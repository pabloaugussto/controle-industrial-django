from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Importamos o modelo de Movimentação do outro app
from estoque.models import Movimentacao 

@login_required(login_url='login')
def index(request):
    # Busca as últimas 5 movimentações FEITAS PELO USUÁRIO LOGADO
    historico_recente = Movimentacao.objects.filter(
        usuario=request.user
    ).order_by('-data')[:5]

    context = {
        'historico': historico_recente
    }
    return render(request, 'core/index.html', context)