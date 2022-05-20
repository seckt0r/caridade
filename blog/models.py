from django.db import models
from django.contrib.auth.models import User

ESTADO = (
    (0, "Rascunho"),
    (1, "Publicado")
)
class Artigo(models.Model):
    titulo = models.CharField(null=True, max_length=300, unique=True)
    slug = models.SlugField(null=True, max_length=300, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='publicacoes')
    conteudo = models.TextField(null=True)
    estado = models.IntegerField(choices=ESTADO, default=0)

    criado_em = models.DateTimeField(null=True, auto_now_add=True)
    atualizado_em = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo
