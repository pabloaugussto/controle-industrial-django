from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    sku = models.CharField(max_length=20, unique=True, verbose_name="Código/SKU")
    localizacao = models.CharField(max_length=50, blank=True, help_text="Ex: Corredor A, Prateleira 2")
    quantidade = models.IntegerField(default=0)
    estoque_minimo = models.IntegerField(default=5, verbose_name="Estoque Mínimo")
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.sku} - {self.nome}"

class Movimentacao(models.Model):
    TIPO_CHOICES = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Responsável")
    observacao = models.CharField(max_length=200, blank=True, verbose_name="Observação")

    class Meta:
        verbose_name = "Movimentação"
        ordering = ['-data']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto.nome}"

    def save(self, *args, **kwargs):
        # Atualiza o saldo do produto automaticamente
        if self.pk is None: 
            if self.tipo == 'E':
                self.produto.quantidade += self.quantidade
            elif self.tipo == 'S':
                if self.produto.quantidade < self.quantidade:
                    raise ValidationError(f"Estoque insuficiente.")
                self.produto.quantidade -= self.quantidade
            self.produto.save()
        super().save(*args, **kwargs)