from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import MovimentacaoForm # <--- Importe o form novo aqui

def lista_produtos(request):
    # Busca todos os produtos ordenados pelo nome
    produtos = Produto.objects.all().order_by('nome')
    
    # Lógica simples de filtro (Search Bar)
    query = request.GET.get('q')
    if query:
        produtos = produtos.filter(nome__icontains=query)

    context = {
        'produtos': produtos,
    }
    return render(request, 'estoque/lista_produtos.html', context)

# Mantenha as outras views (movimentar, historico) como estavam por enquanto
def movimentar(request):
    return render(request, 'estoque/movimentar.html')

def historico(request):
    return render(request, 'estoque/historico.html')

@login_required
def movimentar(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            try:
                # Protocolo: Associa o usuário logado antes de salvar
                movimentacao = form.save(commit=False)
                movimentacao.usuario = request.user
                movimentacao.save() # Aqui o cálculo automático acontece
                
                tipo_desc = dict(movimentacao.TIPO_CHOICES)[movimentacao.tipo]
                messages.success(request, f"{tipo_desc} de {movimentacao.quantidade} itens realizada com sucesso!")
                return redirect('estoque:lista_produtos')
                
            except Exception as e:
                # Captura erro de estoque negativo (ValidationError)
                messages.error(request, f"Erro na operação: {e}")
    else:
        form = MovimentacaoForm()

    context = {
        'form': form
    }
    return render(request, 'estoque/movimentar.html', context)