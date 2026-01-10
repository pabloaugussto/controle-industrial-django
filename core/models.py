from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extensão do Usuário para guardar Cargo e Matrícula
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    matricula = models.CharField(max_length=20, verbose_name="Matrícula/Registro", default="0000")
    cargo = models.CharField(max_length=50, verbose_name="Função/Cargo", default="Colaborador")
    foto = models.ImageField(upload_to='perfis/', null=True, blank=True) # Opcional: para foto futura

    def __str__(self):
        return f"Perfil de {self.user.username}"

# Gatilho: Quando criar um User, cria um Perfil automaticamente
@receiver(post_save, sender=User)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def salvar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()