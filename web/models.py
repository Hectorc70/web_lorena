from django.db import models

# Create your models here.
class LifeInsurance(models.Model):
    id_l           = models.AutoField(primary_key=True, db_column='Id')
    name_full      = models.CharField('Nombre', blank=False, max_length=100,  db_column='NameFull')
    date_of_birth  = models.CharField('Fecha de Nacimiento', blank=False, max_length=48,  db_column='DateOfBirth')
    sex            = models.CharField('Sexo', blank=False, max_length=10,  db_column='Sex')
    marital_status = models.CharField('Estado Civil', blank=False, max_length=10,  db_column='MaritalStatus')
    nationality    = models.CharField('Nacionalidad', blank=False, max_length=20,  db_column='Nationality')
    profession     = models.CharField('Profesion', blank=False, max_length=48,  db_column='Profession')
    postal_code    = models.CharField('Codigo Postal', blank=False, max_length=10,  db_column='PostalCode')
    address        = models.CharField('Direccion', blank=False, max_length=48,  db_column='Address')
    email          = models.EmailField('Correo Electronico', blank=False, max_length=48,  db_column='Email')
    num_phone      = models.CharField('Numero de Whatsapp', blank=False, max_length=10,  db_column='NumPhone')
    weight         = models.FloatField('Peso', blank=False, db_column='Weight')
    height         = models.FloatField('Estatura', blank=False, db_column='Height')
    smoker         = models.BooleanField('Fumador', blank=False, db_column='Smoker')
    sick           = models.BooleanField('Enfermo', blank=False, db_column='sick')
    type_insurance = models.CharField('Tipo de Seguro', blank=False, max_length=48,  db_column='TypeInsurance')
    mount_year     = models.CharField('Monto a Invertir Anualmente', blank=False, max_length=100, db_column='MountYear')
    comments       = models.CharField('Comentarios Adicionales', blank=True, null=False, max_length=300, db_column='Comments')

    class Meta:
        verbose_name = "Seguro de Vida"
        verbose_name_plural = "Seguros de Vida"
        db_table = "Life_Insurance"

    
class InsuranceCar(models.Model):
    id_car              = models.AutoField(primary_key=True, db_column='Id')
    vehicle_type        = models.CharField('Tipo de Vehículo', blank=False, max_length=48,  db_column='vehicleType')
    model               = models.CharField('Modelo', blank=False, max_length=48,  db_column='Modelo')
    description_vehicle = models.CharField('Descripción del Vehículo', blank=False, max_length=100,  db_column='DescriptionVehicle')
    coverage_type       = models.CharField('Tipo de Cobertura', blank=False, max_length=48,  db_column='CoverageType')
    coverage_optional   = models.CharField('Coberturas Opcionales', blank=False, max_length=200,  db_column='CoverageOptional')
    name_full           = models.CharField('Nombre Completo', blank=False, max_length=100,  db_column='NameFull')
    date_of_birth       = models.CharField('Fecha de Nacimiento', blank=False, max_length=48,  db_column='DateOfBirth')
    sex                 = models.CharField('Sexo', blank=False, max_length=10,  db_column='Sex')
    postal_code    = models.CharField('Codigo Postal', blank=False, max_length=10,  db_column='PostalCode')
    email          = models.EmailField('Correo Electronico', blank=False, max_length=48,  db_column='Email')
    num_phone        = models.CharField('Numero de Whatsapp', blank=False, max_length=10,  db_column='NumPhone')
    comments       = models.CharField('Comentarios Adicionales', blank=True, null=True, max_length=300, db_column='Comments')


    class Meta:
        verbose_name = "Seguro de Auto y Motocicleta"
        verbose_name_plural = "Seguro de Autos y Motocicletas"
        db_table = "Insurance_Car"



class InsuranceHouse(models.Model):
    id_house        = models.AutoField(primary_key=True, db_column='Id')
    street          = models.CharField('Calle', blank=False, max_length=48,  db_column='Street')
    number          = models.CharField('Numero', blank=False, max_length=48,  db_column='Number')
    suburb          = models.CharField('Colonia', blank=False, max_length=48,  db_column='Suburb')
    postal_code     = models.CharField('Codigo Postal', blank=False, max_length=10,  db_column='PostalCode')
    city            = models.CharField('Ciudad', blank=False, max_length=48,  db_column='City')
    state           = models.CharField('Estado', blank=False, max_length=48,  db_column='State')
    housing_type    = models.CharField('Tipo de Vivienda', blank=False, max_length=48,  db_column='HousingType')
    year_house      = models.CharField('Año de construcción de vivienda', blank=False, max_length=4,  db_column='YearHouse')
    coverage_type   = models.CharField('Tipo de Cobertura', blank=False, max_length=48,  db_column='CoverageType')
    house_in_river  = models.BooleanField('Casa cerca de Rio', blank=False, db_column='houseInRiver')
    security_measures  = models.CharField('Medidas de Seguridad', max_length=100, blank=False, db_column='SecurityMeasures')
    name_full       = models.CharField('Nombre Completo', blank=False, max_length=100,  db_column='NameFull')
    contract_type   = models.CharField('Tipo de Contratante', blank=False, max_length=48,  db_column='ContractType')
    email           = models.EmailField('Correo Electronico', blank=False, max_length=48,  db_column='Email')
    num_phone       = models.CharField('Numero de Whatsapp', blank=False, max_length=10,  db_column='NumPhone')
    comments       = models.CharField('Comentarios Adicionales', blank=True, null=False, max_length=300, db_column='Comments')



    class Meta:
        verbose_name = "Seguro de Casa Habitacion"
        verbose_name_plural = "Seguro de Casas Habitacion"
        db_table = "Insurance_House"


class MedicalExpenses(models.Model):
    id_e           = models.AutoField(primary_key=True, db_column='Id')
    name_full      = models.CharField('Nombre', blank=False, max_length=100,  db_column='NameFull')
    date_of_birth  = models.CharField('Fecha de Nacimiento', blank=False, max_length=48,  db_column='DateOfBirth')
    sex            = models.CharField('Sexo', blank=False, max_length=10,  db_column='Sex')
    marital_status = models.CharField('Estado Civil', blank=False, max_length=10,  db_column='MaritalStatus')
    nationality    = models.CharField('Nacionalidad', blank=False, max_length=20,  db_column='Nationality')
    profession     = models.CharField('Profesion', blank=False, max_length=48,  db_column='Profession')
    postal_code    = models.CharField('Codigo Postal', blank=False, max_length=10,  db_column='PostalCode')
    address        = models.CharField('Direccion', blank=False, max_length=48,  db_column='Address')
    email          = models.EmailField('Correo Electronico', blank=False, max_length=48,  db_column='Email')
    num_phone      = models.CharField('Numero de Whatsapp', blank=False, max_length=10,  db_column='NumPhone')
    weight         = models.FloatField('Peso', blank=False, db_column='Weight')
    height         = models.FloatField('Estatura', blank=False, db_column='Height')
    parentDiabetes = models.BooleanField('Diabetes', blank=False, db_column='ParentDiabetes')
    sick           = models.CharField('Enfermedad', max_length=100, blank=False, db_column='sick')
    comments       = models.CharField('Comentarios Adicionales', blank=True, null=False, max_length=300, db_column='Comments')

    class Meta:
        verbose_name = "Gastos Medicos"
        verbose_name_plural = "Gastos Medicos"
        db_table = "Medical_Expenses"
