# Generated by Django 5.1.7 on 2025-03-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_usuario_contrasena'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
