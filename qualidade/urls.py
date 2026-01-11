from django.urls import path
from . import views

app_name = 'qualidade'

urlpatterns = [
    # Mantemos apenas a rota de criar auditoria
    path('auditoria/nova/', views.nova_auditoria, name='nova_auditoria'),

]