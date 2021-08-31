# Generated by Django 3.0.2 on 2021-08-31 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20210829_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCar',
            fields=[
                ('id_car', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(db_column='vehicleType', max_length=48, verbose_name='Tipo de Vehículo')),
                ('model', models.CharField(db_column='Modelo', max_length=48, verbose_name='Modelo')),
                ('description_vehicle', models.CharField(db_column='DescriptionVehicle', max_length=100, verbose_name='Descripción del Vehículo')),
                ('coverage_type', models.CharField(db_column='CoverageType', max_length=48, verbose_name='Tipo de Cobertura')),
                ('coverage_optional', models.CharField(db_column='CoverageOptional', max_length=48, verbose_name='Coberturas Opcionales')),
                ('name_full', models.CharField(db_column='NameFull', max_length=100, verbose_name='Nombre Completo')),
                ('date_of_birth', models.CharField(db_column='DateOfBirth', max_length=48, verbose_name='Fecha de Nacimiento')),
                ('sex', models.CharField(db_column='Sex', max_length=10, verbose_name='Sexo')),
                ('postal_code', models.CharField(db_column='PostalCode', max_length=10, verbose_name='Codigo Postal')),
                ('email', models.EmailField(db_column='Email', max_length=48, verbose_name='Correo Electronico')),
                ('num_cel', models.CharField(db_column='NumPhone', max_length=10, verbose_name='Numero de Whatsapp')),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=300, verbose_name='Comentarios Adicionales')),
            ],
            options={
                'verbose_name': 'Seguro de Auto y Motocicleta',
                'verbose_name_plural': 'Seguro de Autos y Motocicletas',
                'db_table': 'Insurance_Car',
            },
        ),
        migrations.CreateModel(
            name='InsuranceHouse',
            fields=[
                ('id_house', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('street', models.CharField(db_column='Street', max_length=48, verbose_name='Calle')),
                ('number', models.CharField(db_column='Number', max_length=48, verbose_name='Numero')),
                ('suburb', models.CharField(db_column='Suburb', max_length=48, verbose_name='Colonia')),
                ('postal_code', models.CharField(db_column='PostalCode', max_length=10, verbose_name='Codigo Postal')),
                ('municipality', models.CharField(db_column='municipality', max_length=48, verbose_name='Municipio')),
                ('state', models.CharField(db_column='State', max_length=48, verbose_name='Estado')),
                ('housing_type', models.CharField(db_column='HousingType', max_length=48, verbose_name='Tipo de Vivienda')),
                ('year_house', models.CharField(db_column='YearHouse', max_length=4, verbose_name='Año de construcción de vivienda')),
                ('coverage_type', models.CharField(db_column='CoverageType', max_length=48, verbose_name='Tipo de Cobertura')),
                ('house_in_river', models.BooleanField(db_column='houseInRiver', verbose_name='Casa cerca de Rio')),
                ('name_full', models.CharField(db_column='NameFull', max_length=100, verbose_name='Nombre Completo')),
                ('contract_type', models.CharField(db_column='ContractType', max_length=48, verbose_name='Tipo de Contratante')),
                ('email', models.EmailField(db_column='Email', max_length=48, verbose_name='Correo Electronico')),
                ('num_phone', models.CharField(db_column='NumPhone', max_length=10, verbose_name='Numero de Whatsapp')),
                ('comments', models.CharField(blank=True, db_column='Comments', max_length=300, verbose_name='Comentarios Adicionales')),
            ],
            options={
                'verbose_name': 'Seguro de Casa Habitacion',
                'verbose_name_plural': 'Seguro de Casas Habitacion',
                'db_table': 'Insurance_House',
            },
        ),
        migrations.RemoveField(
            model_name='lifeinsurance',
            name='Num_cel',
        ),
        migrations.AddField(
            model_name='lifeinsurance',
            name='num_phone',
            field=models.CharField(db_column='NumPhone', default=0, max_length=10, verbose_name='Numero de Whatsapp'),
            preserve_default=False,
        ),
    ]
