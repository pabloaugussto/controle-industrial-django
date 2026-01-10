from django.contrib import admin
from .models import Questao, Auditoria, Resposta

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('texto', 'senso', 'ativo')
    list_filter = ('senso',)

class RespostaInline(admin.TabularInline):
    model = Resposta
    extra = 0
    readonly_fields = ('questao', 'conforme', 'foto')
    can_delete = False

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('setor', 'data', 'usuario', 'nota_final')
    list_filter = ('setor', 'data')
    inlines = [RespostaInline] # Permite ver as respostas dentro da auditoria no Admin