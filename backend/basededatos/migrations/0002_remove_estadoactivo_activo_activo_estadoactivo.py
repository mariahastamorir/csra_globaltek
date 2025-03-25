# Generated by Django 5.1.7 on 2025-03-25 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basededatos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadoactivo',
            name='activo',
        ),
        migrations.AddField(
            model_name='activo',
            name='estadoActivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basededatos.estadoactivo'),
        ),
    ]
