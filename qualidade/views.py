from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Questao, Auditoria, Resposta
from .forms import AuditoriaForm
import json
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta

@login_required
def nova_auditoria(request):
    # Busca apenas perguntas ativas para exibir na tela
    questoes = Questao.objects.filter(ativo=True).order_by('senso')

    if request.method == 'POST':
        form = AuditoriaForm(request.POST)
        if form.is_valid():
            try:
                # 1. Salva o Cabeçalho da Auditoria
                auditoria = form.save(commit=False)
                auditoria.usuario = request.user
                auditoria.save()

                # 2. Varre as perguntas para salvar as respostas individuais
                for questao in questoes:
                    # No HTML, vamos nomear os campos como 'status_ID' e 'foto_ID'
                    status_input = request.POST.get(f'status_{questao.id}')
                    foto_input = request.FILES.get(f'foto_{questao.id}')
                    
                    # Se status for 'true', é Conforme. Se for 'false', Não Conforme.
                    eh_conforme = (status_input == 'true')

                    Resposta.objects.create(
                        auditoria=auditoria,
                        questao=questao,
                        conforme=eh_conforme,
                        foto=foto_input
                    )

                # 3. Calcula a nota final e exibe mensagem
                nota = auditoria.calcular_nota()
                messages.success(request, f"Auditoria finalizada! Nota do setor: {nota:.1f}%")
                return redirect('dashboard') # Por enquanto volta pro Dash

            except Exception as e:
                messages.error(request, f"Erro ao salvar: {e}")
    else:
        form = AuditoriaForm()

    context = {
        'form': form,
        'questoes': questoes
    }
    return render(request, 'qualidade/nova_auditoria.html', context)



@login_required
def relatorios(request):
    # 1. Define o intervalo da Semana Atual (Segunda a Domingo)
    hoje = timezone.now().date()
    inicio_semana = hoje - timedelta(days=hoje.weekday()) # Pega a segunda-feira
    
    # 2. Busca auditorias dessa semana
    auditorias_semana = Auditoria.objects.filter(data__gte=inicio_semana)
    
    # 3. Calcula a Média Geral da Semana
    media_semanal = auditorias_semana.aggregate(Avg('nota_final'))['nota_final__avg'] or 0

    # 4. Prepara dados para o Gráfico (Evolução Diária)
    # Vamos criar um dicionário para os 7 dias da semana
    dados_grafico = []
    labels_grafico = []
    
    for i in range(7):
        dia = inicio_semana + timedelta(days=i)
        # Filtra auditorias daquele dia específico
        auditorias_dia = auditorias_semana.filter(data__date=dia)
        media_dia = auditorias_dia.aggregate(Avg('nota_final'))['nota_final__avg'] or 0
        
        labels_grafico.append(dia.strftime("%d/%m")) # Ex: 31/12
        dados_grafico.append(float(round(media_dia, 2)))

    # 5. Ranking por Setor (Média Acumulada)
    ranking = []
    for codigo, nome in Auditoria.SETOR_CHOICES:
        media_setor = Auditoria.objects.filter(setor=codigo).aggregate(Avg('nota_final'))['nota_final__avg'] or 0
        ranking.append({'nome': nome, 'media': media_setor})
    
   # Ordena do maior para o menor
    ranking.sort(key=lambda x: x['media'], reverse=True)

    # CORREÇÃO: Pegamos o melhor e o pior aqui no Python
    # O ranking[0] é o melhor (maior nota)
    # O ranking[-1] é o pior (menor nota), funciona mesmo se tiverem poucos setores
    melhor_setor = ranking[0]
    pior_setor = ranking[-1]

    context = {
        'media_semanal': media_semanal,
        'ranking': ranking,
        'melhor_setor': melhor_setor, # Passamos pronto pro HTML
        'pior_setor': pior_setor,     # Passamos pronto pro HTML
        'auditorias_recentes': Auditoria.objects.order_by('-data')[:5],
        'chart_labels': json.dumps(labels_grafico),
        'chart_data': json.dumps(dados_grafico),
    }
    
    return render(request, 'qualidade/relatorios.html', context)