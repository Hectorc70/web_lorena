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
    Num_cel        = models.CharField('Numero de Whatsapp', blank=False, max_length=10,  db_column='NumCel')
    weight         = models.FloatField('Peso', blank=False, db_column='Weight')
    height         = models.FloatField('Estatura', blank=False, db_column='Height')
    smoker         = models.BooleanField('Fumador', blank=False, db_column='Smoker')
    sick           = models.BooleanField('Enfermo', blank=False, db_column='sick')
    type_insurance = models.CharField('Tipo de Seguro', blank=False, max_length=48,  db_column='TypeInsurance')
    mount_year     = models.CharField('Monto a Invertir Anualmente', blank=False, max_length=100, db_column='MountYear')
    comments       = models.CharField('Comentarios Adicionales', blank=True, null=False, max_length=300, db_column='Comments')


