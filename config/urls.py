from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rotas dos Apps
    path('', include('core.urls')),        # Raiz (Login/Dash)
    path('estoque/', include('estoque.urls')),
    path('5s/', include('qualidade.urls')), # Prefixo '5s' fica mais curto na URL
]

# Configuração para servir imagens (Media) durante desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)