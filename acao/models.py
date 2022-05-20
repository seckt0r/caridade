from django.db import models
from django.contrib.auth.models import User

class Doacao(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True, help_text="Nome completo do doador", verbose_name="Nome completo")
    telefone = models.IntegerField(null=True, blank=True, help_text="Número de telefone do doador. Apenas números", verbose_name="Telefone")
    descricao = models.TextField(null=True, blank=True, help_text="Descrição do tipo de ajuda a disponibilizar", verbose_name="Descrição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Doações"

class Solicitacao(models.Model):
    """
    As informações que serão submetidas para descrever o tipo de ajuda que é necessária e a quem deve ser prestada a ajuda
    
    numero # numeração de controle do pedido. Deve ser gerado programaticamente
    categoria # ajuda monetária, aconselhamento, ensino/educação, outros bens materiais
    descricao # descrição detalhada do tipo de ajuda que se necessita
    prioridade # definição da prioridade. A ser definido pelos operadores do serviço
    """
    nome_autor = models.CharField(max_length=100, null=True, blank=True, help_text="Nome completo de quem submete a solicitação doador", verbose_name="Nome completo")
    telefone_autor = models.IntegerField(null=True, blank=True, help_text="Número de telefone do doador. Apenas números", verbose_name="Telefone")
    nome_necessitado = models.CharField(max_length=100, null=True, blank=True, help_text="Nome completo da pessoa necessitada", verbose_name="Nome completo da pessoa necessitada")
    telefone_necessitado = models.IntegerField(null=True, blank=True, help_text="Número de telefone da pessoa necessitada. Apenas números", verbose_name="Telefone da pessoa necessitada")
    descricao = models.TextField(null=True, blank=True, help_text="Descrição do tipo de ajuda a disponibilizar", verbose_name="Descrição")

    def __str__(self):
        return self.nome_necessitado
    class Meta:
        verbose_name_plural = "Solicitações"

class Colaboracao(models.Model):
    """
    As informações dos voluntários
    """
    nome = models.CharField(max_length=100, null=True, blank=True, help_text="Nome completo do colaborador", verbose_name="Nome completo")
    telefone = models.IntegerField(null=True, blank=True, help_text="Número de telefone do colaborador. Apenas números", verbose_name="Telefone")
    descricao = models.TextField(null=True, blank=True, help_text="Descreva como pode colaborar", verbose_name="Descrição")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Colaborações"