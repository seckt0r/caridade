# Generated by Django 4.0.4 on 2022-05-21 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_artigo_options_artigo_atualizado_em_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.CharField(max_length=300, null=True, unique=True, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='imagem',
            field=models.ImageField(null=True, upload_to='', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='publicacoes', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='conteudo',
            field=models.TextField(null=True, verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='estado',
            field=models.IntegerField(choices=[(0, 'Rascunho'), (1, 'Publicado')], default=0, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='slug',
            field=models.SlugField(max_length=300, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='titulo',
            field=models.CharField(max_length=300, null=True, unique=True, verbose_name='Título'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField(null=True, verbose_name='Conteúdo')),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Artigo', to='blog.artigo', verbose_name='Artigo')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
    ]