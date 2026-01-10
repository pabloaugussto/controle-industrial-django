from django.urls import path
from . import views

app_name = 'estoque' # Importante para usar {% url 'estoque:lista' %}

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('movimentar/', views.movimentar, name='movimentar'),
    path('historico/', views.historico, name='historico'),
]