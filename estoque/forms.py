from django import forms
from .models import Movimentacao

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto', 'tipo', 'quantidade', 'observacao']
        widgets = {
            'produto': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'tipo': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'}),
            'quantidade': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500', 'min': '1'}),
            'observacao': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500', 'placeholder': 'Ex: NF 1234 ou Setor de Solda'}),
        }
        labels = {
            'observacao': 'Justificativa / Documento'
        }