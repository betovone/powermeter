# Generated by Django 4.1.5 on 2023-01-17 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llave', models.CharField(max_length=50, unique=True, verbose_name='Llave identificadora')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha-Hora')),
                ('consumo', models.PositiveIntegerField(verbose_name='Consumo (kwh)')),
                ('medidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medidor.medidor')),
            ],
        ),
    ]
