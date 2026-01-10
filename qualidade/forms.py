from django import forms
from .models import Auditoria

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = ['setor', 'observacao']
        widgets = {
            'setor': forms.Select(attrs={'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 bg-white'}),
            'observacao': forms.Textarea(attrs={'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500', 'rows': 3, 'placeholder': 'Alguma observação geral sobre a auditoria?'}),
        }