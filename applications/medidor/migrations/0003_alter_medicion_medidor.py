# Generated by Django 4.1.5 on 2023-01-17 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medidor', '0002_alter_medicion_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicion',
            name='medidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicion', to='medidor.medidor'),
        ),
    ]
