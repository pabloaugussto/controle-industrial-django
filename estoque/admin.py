from django.contrib import admin
from .models import Categoria, Produto, Movimentacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Colunas que vão aparecer na lista
    list_display = ('sku', 'nome', 'quantidade', 'localizacao', 'estoque_minimo')
    # Campos que permitem busca
    search_fields = ('nome', 'sku')
    # Filtro lateral
    list_filter = ('categoria',)

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'tipo', 'quantidade', 'usuario', 'data')
    list_filter = ('tipo', 'data', 'usuario')
    # Cria uma caixa de busca para selecionar o produto (útil quando tem muitos itens)
    autocomplete_fields = ['produto']