# Generated by Django 4.2.2 on 2023-06-16 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_autor_autor_post_contenido_post_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='Autor',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
