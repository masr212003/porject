# Generated by Django 4.2.11 on 2024-10-14 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iniusuario', '0007_rename_usuario_datosusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosusuario',
            name='password',
        ),
    ]
