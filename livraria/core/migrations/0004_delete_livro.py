# Generated by Django 4.1 on 2022-09-09 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_autor_options_livro'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Livro',
        ),
    ]
