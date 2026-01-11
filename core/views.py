from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from datetime import timedelta
import json
from django.core.serializers.json import DjangoJSONEncoder

# Importação dos Modelos
from estoque.models import Movimentacao
from qualidade.models import Auditoria

@login_required
def index(request):
    # 1. SIDEBAR: Histórico Recente
    historico_recente = Movimentacao.objects.filter(
        usuario=request.user
    ).select_related('produto').order_by('-data')[:5]

    # --- LÓGICA DO DASHBOARD DE QUALIDADE ---
    
    # 2. Definir o período (Semana Atual)
    hoje = timezone.now()
    inicio_semana = hoje - timedelta(days=hoje.weekday()) # Pega a segunda-feira
    
    # CORREÇÃO AQUI: Mudamos de 'data_auditoria' para 'data'
    auditorias_semana = Auditoria.objects.filter(data__gte=inicio_semana)

    # 3. KPI: Média Geral da Semana
    media_semanal = auditorias_semana.aggregate(m=Avg('nota_final'))['m'] or 0

    # 4. KPI & Ranking: Agrupar por Setor
    ranking_bruto = auditorias_semana.values('setor').annotate(
        media=Avg('nota_final'),
        total_auditorias=Count('id')
    ).order_by('-media')

    ranking = []
    for item in ranking_bruto:
        # Tenta pegar o nome legível do setor (ex: 'Almoxarifado' em vez de 'ALMOXARIFADO')
        nome_setor = dict(Auditoria.SETOR_CHOICES).get(item['setor'], item['setor'])
        ranking.append({'nome': nome_setor, 'media': item['media']})

    # 5. Melhores e Piores
    melhor_setor = ranking[0] if ranking else None
    pior_setor = ranking[-1] if ranking else None

    # 6. Dados para o Gráfico (Evolução Diária)
    # CORREÇÃO AQUI TAMBÉM: Usando 'data' no TruncDate
    dados_diarios = auditorias_semana.annotate(
        dia=TruncDate('data')
    ).values('dia').annotate(
        media_dia=Avg('nota_final')
    ).order_by('dia')

    chart_labels = [d['dia'].strftime('%d/%m') for d in dados_diarios]
    chart_data = [round(d['media_dia'], 1) for d in dados_diarios]

    # --- CONTEXTO FINAL ---
    context = {
        'historico': historico_recente,
        'media_semanal': media_semanal,
        'melhor_setor': melhor_setor,
        'ranking': ranking,
        'chart_labels': json.dumps(chart_labels, cls=DjangoJSONEncoder),
        'chart_data': json.dumps(chart_data, cls=DjangoJSONEncoder),
    }
    
    return render(request, 'core/index.html', context)