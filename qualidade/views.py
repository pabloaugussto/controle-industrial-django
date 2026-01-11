from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Questao, Auditoria, Resposta
from .forms import AuditoriaForm
import json
from django.db.models import Avg
from django.utils import timezone
from datetime import timedelta
from django.db.models import Case, When, Value, IntegerField

@login_required
def nova_auditoria(request):
    # --- MUDANÇA AQUI: Ordenação forçada (1S -> 5S) ---
    questoes = Questao.objects.filter(ativo=True).annotate(
        ordem_logica=Case(
            When(senso='SEIRI', then=Value(1)),    # 1. Utilização
            When(senso='SEITON', then=Value(2)),   # 2. Ordenação
            When(senso='SEISO', then=Value(3)),    # 3. Limpeza
            When(senso='SEIKETSU', then=Value(4)), # 4. Padronização
            When(senso='SHITSUKE', then=Value(5)), # 5. Disciplina
            default=Value(6),
            output_field=IntegerField(),
        )
    ).order_by('ordem_logica')
    # --------------------------------------------------

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
                    status_input = request.POST.get(f'status_{questao.id}')
                    foto_input = request.FILES.get(f'foto_{questao.id}')
                    
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
                return redirect('qualidade:relatorios') # Ajustei para ir para relatórios, mas pode manter dashboard se preferir

            except Exception as e:
                messages.error(request, f"Erro ao salvar: {e}")
    else:
        form = AuditoriaForm()

    context = {
        'form': form,
        'questoes': questoes
    }
    return render(request, 'qualidade/nova_auditoria.html', context)



