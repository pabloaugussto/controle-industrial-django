from django.contrib import admin
from django.urls import path, include # Não esqueça de importar o include!
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- ROTA DA HOME CORRIGIDA ---
    # Agora usamos o arquivo que criamos no passo 1
    path('', include('core.urls')), 
    
    # Suas outras rotas (Mantenha como estão)
    path('estoque/', include('estoque.urls')),
    path('5s/', include('qualidade.urls')),
    
    # Rotas de Login (Mantenha como estão, parecem estar funcionando)
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]