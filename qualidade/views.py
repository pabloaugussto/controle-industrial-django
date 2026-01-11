from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import os
from django.conf import settings
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
                return redirect('core:index') # Ajustei para ir para relatórios, mas pode manter dashboard se preferir

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
def historico_auditorias(request):
    # Lista as auditorias da mais recente para a mais antiga
    auditorias = Auditoria.objects.filter(usuario=request.user).order_by('-data')
    return render(request, 'qualidade/historico.html', {'auditorias': auditorias})

@login_required
def gerar_pdf(request, pk):
    # Busca a auditoria pelo ID (pk)
    auditoria = Auditoria.objects.get(id=pk)
    
    # Prepara o contexto (dados que vão pro PDF)
    context = {'auditoria': auditoria}
    
    # Carrega o template HTML do PDF
    template_path = 'qualidade/pdf_template.html'
    template = get_template(template_path)
    html = template.render(context)

    # Cria a resposta do Django como PDF
    response = HttpResponse(content_type='application/pdf')
    # Se quiser que baixe direto, mude 'inline' para 'attachment'
    response['Content-Disposition'] = f'inline; filename="Auditoria_{auditoria.id}.pdf"'

    # Gera o PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Tivemos erros ao gerar o PDF <pre>' + html + '</pre>')
    return response

@login_required
def deletar_auditoria(request, pk):
    # Busca a auditoria apenas se ela pertencer ao usuário logado (segurança)
    auditoria = get_object_or_404(Auditoria, pk=pk, usuario=request.user)
    
    auditoria.delete()
    messages.success(request, "Auditoria excluída com sucesso!")
    
    return redirect('qualidade:historico')



