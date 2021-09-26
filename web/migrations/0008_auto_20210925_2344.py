# Generated by Django 3.0.2 on 2021-09-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20210925_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancehouse',
            name='security_measures',
            field=models.CharField(db_column='SecurityMeasures', default=1, max_length=100, verbose_name='Medidas de Seguridad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='insurancecar',
            name='comments',
            field=models.CharField(blank=True, db_column='Comments', max_length=300, null=True, verbose_name='Comentarios Adicionales'),
        ),
        migrations.AlterField(
            model_name='insurancecar',
            name='coverage_optional',
            field=models.CharField(db_column='CoverageOptional', max_length=200, verbose_name='Coberturas Opcionales'),
        ),
    ]
