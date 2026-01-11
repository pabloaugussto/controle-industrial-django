from django.urls import path
from . import views

# AQUI ESTÁ A SOLUÇÃO: Definimos o "sobrenome" do app
app_name = 'core' 

urlpatterns = [
    # Agora essa rota se chama oficialmente 'core:index'
    path('', views.index, name='index'),
]