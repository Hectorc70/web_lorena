# Generated by Django 3.0.2 on 2021-09-12 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210830_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalExpenses',
            fields=[
                ('id_e', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name_full', models.CharField(db_column='NameFull', max_length=100, verbose_name='Nombre')),
                ('date_of_birth', models.CharField(db_column='DateOfBirth', max_length=48, verbose_name='Fecha de Nacimiento')),
                ('sex', models.CharField(db_column='Sex', max_length=10, verbose_name='Sexo')),
                ('marital_status', models.CharField(db_column='MaritalStatus', max_length=10, verbose_name='Estado Civil')),
                ('nationality', models.CharField(db_column='Nationality', max_length=20, verbose_name='Nacionalidad')),
                ('profession', models.CharField(db_column='Profession', max_length=48, verbose_name='Profesion')),
                ('postal_code', models.CharField(db_column='PostalCode', max_length=10, verbose_name='Codigo Postal')),
                ('address', models.CharField(db_column='Address', max_length=48, verbose_name='Direccion')),
                ('email', models.EmailField(db_column='Email', max_length=48, verbose_name='Correo Electronico')),
                ('num_phone', models.CharField(db_column='NumPhone', max_length=10, verbose_name='Numero de Whatsapp')),
                ('weight', models.FloatField(db_column='Weight', verbose_name='Peso')),
                ('height', models.FloatField(db_column='Height', verbose_name='Estatura')),
                ('parentDiabetes', models.BooleanField(db_column='ParentDiabetes', verbose_name='Diabetes')),
                ('sick', models.CharField(db_column='sick', max_length=100, verbose_name='Enfermedad')),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=300, verbose_name='Comentarios Adicionales')),
            ],
            options={
                'verbose_name': 'Gastos Medicos',
                'verbose_name_plural': 'Gastos Medicos',
                'db_table': 'Medical_Expenses',
            },
        ),
    ]