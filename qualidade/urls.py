from django.urls import path
from . import views

app_name = 'qualidade'

urlpatterns = [
    # O link do card procura por este nome='relatorios'
    path('relatorios/', views.relatorios, name='relatorios'),
    
    path('auditoria/nova/', views.nova_auditoria, name='nova_auditoria'),
]