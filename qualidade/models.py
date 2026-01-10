from django.db import models
from django.contrib.auth.models import User

class Questao(models.Model):
    SENSO_CHOICES = (
        ('SEIRI', '1. Seiri (Utilização)'),
        ('SEITON', '2. Seiton (Ordenação)'),
        ('SEISO', '3. Seiso (Limpeza)'),
        ('SEIKETSU', '4. Seiketsu (Padronização)'),
        ('SHITSUKE', '5. Shitsuke (Disciplina)'),
    )
    texto = models.CharField(max_length=255, verbose_name="Pergunta")
    senso = models.CharField(max_length=20, choices=SENSO_CHOICES)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.senso}] {self.texto}"

    class Meta:
        verbose_name = "Pergunta do Checklist"
        verbose_name_plural = "Perguntas do Checklist"

class Auditoria(models.Model):
    SETOR_CHOICES = (
        ('PRODUCAO', 'Produção'),
        ('ALMOXARIFADO', 'Almoxarifado'),
        ('MANUTENCAO', 'Manutenção'),
        ('ESCRITORIO', 'Escritório/Adm'),
    )
    
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    setor = models.CharField(max_length=20, choices=SETOR_CHOICES)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, verbose_name="Observações Gerais")
    nota_final = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Auditoria {self.setor} - {self.data.strftime('%d/%m/%Y')}"
    
    def calcular_nota(self):
        # Pega todas as respostas vinculadas a esta auditoria
        respostas = self.resposta_set.all()
        total = respostas.count()
        if total == 0:
            return 0
        
        conformes = respostas.filter(conforme=True).count()
        nota = (conformes / total) * 100
        
        self.nota_final = nota
        self.save()
        return nota

class Resposta(models.Model):
    auditoria = models.ForeignKey(Auditoria, on_delete=models.CASCADE)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    conforme = models.BooleanField(default=False, verbose_name="Está conforme?")
    foto = models.ImageField(upload_to='auditorias/', null=True, blank=True, verbose_name="Evidência (Foto)")

    def __str__(self):
        return f"{self.questao.texto} - {'OK' if self.conforme else 'NOK'}"