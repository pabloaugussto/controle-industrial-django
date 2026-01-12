from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from qualidade.models import Auditoria

@login_required
def index(request):
    # --- 1. CONFIGURAÇÃO DE DATAS ---
    hoje = timezone.now()
    
    # Define o início desta semana (Segunda-feira) para os KPIs
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    inicio_semana = inicio_semana.replace(hour=0, minute=0, second=0, microsecond=0)

    # --- 2. CÁLCULO DOS KPIS (MÉDIAS DA SEMANA) ---
    auditorias_semana = Auditoria.objects.filter(data__gte=inicio_semana)

    # Média Geral da Semana
    media_semanal = auditorias_semana.aggregate(Avg('nota_final'))['nota_final__avg'] or 0

    # Ranking por Setor
    stats_setores = auditorias_semana.values('setor').annotate(media=Avg('nota_final')).order_by('-media')
    
    ranking = []
    for item in stats_setores:
        # Pega o nome legível do setor (Ex: 'Almoxarifado' em vez de 'almox')
        # Usa _meta.get_field para garantir que funcione independente do nome da lista
        nome_setor = dict(Auditoria._meta.get_field('setor').choices).get(item['setor'], item['setor'])
        ranking.append({'nome': nome_setor, 'media': item['media']})

    # Define melhor setor (primeiro do ranking)
    melhor_setor = ranking[0] if ranking else None
    
    # --- 3. DADOS PARA O GRÁFICO (Últimos 7 dias) ---
    chart_labels = []
    chart_data = []

    # Loop pelos últimos 7 dias (incluindo hoje)
    for i in range(6, -1, -1):
        dia = hoje - timedelta(days=i)
        
        # Define o intervalo do dia (00:00 até 23:59)
        dia_inicio = dia.replace(hour=0, minute=0, second=0)
        dia_fim = dia.replace(hour=23, minute=59, second=59)

        # Filtra auditorias daquele dia específico
        auditorias_dia = Auditoria.objects.filter(data__range=(dia_inicio, dia_fim))
        
        # Calcula a média do dia
        media_dia = auditorias_dia.aggregate(Avg('nota_final'))['nota_final__avg'] or 0
        
        # Adiciona na lista do gráfico
        chart_labels.append(dia.strftime('%d/%m')) # Ex: 12/01
        
        # --- A CORREÇÃO MÁGICA ESTÁ AQUI ---
        # Convertemos para float() para o JavaScript não travar com "Decimal()"
        chart_data.append(float(round(media_dia, 1)))

    # --- 4. HISTÓRICO RECENTE (SIDEBAR) ---
    historico_recente = Auditoria.objects.all().order_by('-data')[:5]

    context = {
        'media_semanal': media_semanal,
        'ranking': ranking,
        'melhor_setor': melhor_setor,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'historico': historico_recente,
    }

    return render(request, 'core/index.html', context)