# Generated by Django 3.0.2 on 2021-09-26 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_medicalexpenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecar',
            name='coverage_optional',
            field=models.CharField(db_column='CoverageOptional', max_length=100, verbose_name='Coberturas Opcionales'),
        ),
    ]
