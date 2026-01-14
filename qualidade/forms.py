from django import forms
from .models import Auditoria
from .models import Questao

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = ['setor', 'observacao']
        widgets = {
            'setor': forms.Select(attrs={'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 bg-white'}),
            'observacao': forms.Textarea(attrs={'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500', 'rows': 3, 'placeholder': 'Alguma observação geral sobre a auditoria?'}),
        }

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ['senso', 'texto'] # Ajuste se seus campos tiverem outros nomes
        widgets = {
            'senso': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-gray-50'
            }),
            'texto': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all bg-gray-50',
                'placeholder': 'Digite a pergunta da auditoria...'
            })
        }
        labels = {
            'senso': 'A qual Senso (5S) pertence?',
            'texto': 'Pergunta'
        }