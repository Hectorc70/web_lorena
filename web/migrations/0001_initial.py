# Generated by Django 3.0.2 on 2021-08-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LifeInsurance',
            fields=[
                ('id_l', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('name_full', models.CharField(db_column='NameFull', max_length=100, verbose_name='Nombre')),
                ('date_of_birth', models.CharField(db_column='DateOfBirth', max_length=48, verbose_name='Fecha de Nacimiento')),
                ('sex', models.CharField(db_column='Sex', max_length=10, verbose_name='Sexo')),
                ('marital_status', models.CharField(db_column='MaritalStatus', max_length=10, verbose_name='Estado Civil')),
                ('nationality', models.CharField(db_column='Nationality', max_length=20, verbose_name='Nacionalidad')),
                ('profession', models.CharField(db_column='Profession', max_length=48, verbose_name='Profesion')),
                ('postal_code', models.CharField(db_column='PostalCode', max_length=10, verbose_name='Codigo Postal')),
                ('address', models.CharField(db_column='Address', max_length=48, verbose_name='Direccion')),
                ('email', models.EmailField(db_column='Email', max_length=48, verbose_name='Correo Electronico')),
                ('Num_cel', models.CharField(db_column='NumCel', max_length=10, verbose_name='Numero de Whatsapp')),
                ('weight', models.FloatField(db_column='Weight', verbose_name='Peso')),
                ('height', models.FloatField(db_column='Height', verbose_name='Estatura')),
                ('smoker', models.BooleanField(db_column='Smoker', verbose_name='Fumador')),
                ('sick', models.BooleanField(db_column='sick', verbose_name='Enfermo')),
                ('type_insurance', models.CharField(db_column='TypeInsurance', max_length=48, verbose_name='Tipo de Seguro')),
                ('mount_year', models.CharField(db_column='MountYear', max_length=100, verbose_name='Monto a Invertir Anualmente')),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=300, verbose_name='Comentarios Adicionales')),
            ],
        ),
    ]
