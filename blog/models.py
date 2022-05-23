from tabnanny import verbose
#from tinymce_4.fields import TinyMCEModelField
from django.db import models
from django.contrib.auth.models import User


ESTADO = (
    (0, "Rascunho"),
    (1, "Publicado")
)
class Artigo(models.Model):
    titulo = models.CharField(null=True, max_length=300, unique=True, verbose_name='Título')
    slug = models.SlugField(null=True, max_length=300, unique=True, verbose_name='Slug')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='publicacoes', verbose_name='Autor')
    conteudo = models.TextField(null=True, verbose_name='Conteúdo')
    estado = models.IntegerField(choices=ESTADO, default=0, verbose_name='Estado')
    categoria = models.CharField(null=True, max_length=300, unique=True, verbose_name='Categoria')
    imagem = models.ImageField(upload_to='blog/', null=True, verbose_name='Imagem')

    criado_em = models.DateTimeField(null=True, auto_now_add=True)
    atualizado_em = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey('Artigo', related_name='Artigo', on_delete=models.CASCADE, verbose_name='Artigo')
    conteudo = models.TextField(null=True, verbose_name='Conteúdo')
    criado_em = models.DateTimeField(null=True, auto_now_add=True)
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.artigo.titulo