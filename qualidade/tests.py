import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from qualidade.models import Auditoria

# --- TESTE 1: Acesso e Segurança ---
@pytest.mark.django_db
def test_acesso_relatorios(client):
    # 1. Tenta acessar sem login (deve redirecionar 302)
    url = reverse('qualidade:relatorios')
    resp_anonimo = client.get(url)
    assert resp_anonimo.status_code == 302

    # 2. Cria usuário e loga
    usuario = User.objects.create_user(username='tester', password='123')
    client.force_login(usuario)

    # 3. Tenta acessar logado (deve funcionar 200)
    resp_logado = client.get(url)
    assert resp_logado.status_code == 200

# --- TESTE 2: Lógica do Ranking ---
@pytest.mark.django_db
def test_calculo_media_ranking(client):
    # 1. Cria usuário
    user = User.objects.create_user(username='auditor', password='123')
    client.force_login(user)

    # 2. Cria duas Auditorias no banco de teste
    Auditoria.objects.create(usuario=user, setor='ALMOXARIFADO', nota_final=100)
    Auditoria.objects.create(usuario=user, setor='PRODUCAO', nota_final=50)
    # Nota: Escritório e Manutenção ficarão com nota 0.0 pois não criamos auditoria para eles

    # 3. Acessa o dashboard
    url = reverse('qualidade:relatorios')
    response = client.get(url)
    
    # 4. Recupera os dados do contexto
    melhor = response.context['melhor_setor']
    pior = response.context['pior_setor']
    ranking = response.context['ranking']

    # VERIFICAÇÃO 1: O Melhor deve ser Almoxarifado (100)
    assert melhor['nome'] == 'Almoxarifado'
    assert melhor['media'] == 100.0
    
    # VERIFICAÇÃO 2: O Pior deve ter nota 0.0 (pois existem setores vazios)
    # O erro acontecia aqui porque 0.0 < 50.0
    assert pior['media'] == 0.0
    
    # VERIFICAÇÃO 3: Vamos garantir que a Produção foi calculada certa (50.0)
    # Procuramos 'Produção' dentro da lista de ranking
    dados_producao = next(item for item in ranking if item['nome'] == 'Produção')
    assert dados_producao['media'] == 50.0