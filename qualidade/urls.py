from django.urls import path
from . import views

app_name = 'qualidade'

urlpatterns = [
    # Mantemos apenas a rota de criar auditoria
    path('auditoria/nova/', views.nova_auditoria, name='nova_auditoria'),
    path('historico/', views.historico_auditorias, name='historico'),
    path('pdf/<int:pk>/', views.gerar_pdf, name='gerar_pdf'),
    path('excluir/<int:pk>/', views.deletar_auditoria, name='deletar_auditoria'),

]