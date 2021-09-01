from django import forms
from django.forms import widgets
from django.forms import Textarea

from .models import *


class DateTimeInput(forms.DateInput):
    input_type = 'date'

class LifeInsuranceForm(forms.ModelForm):
    class Meta:
        model = LifeInsurance
        fields = '__all__'
        exclude = ['id_l']
        widgets = {
                'date_of_birth':DateTimeInput(),

                'sex':forms.Select(choices=(('',''),('masculino','Masculino'), 
                ('femenino','Femenino'), 
                ('sin especificar','Sin Especificar'))
                ),

                'marital_status':forms.Select(choices=(('',''),('solter@','Solter@'), 
                ('casado','Casad@'), ('divorciad@','Divorciad@'), ('viud@','Viud@'),
                ('concubinato','Concubinato')
                )),

                'type_insurance':forms.Select(choices=(('',''),
                ('ahorro','Para el Ahorro (imagina recibir después de 10 años los ingresos para cumplir tus sueños)'), 
                ('retiro','Para el Retiro (cuando termines de trabajar recibir rentas vitalicias para vivir tu retiro)'), 
                ('educacion','Para la Educación de menores (empieza el proyecto de educación para tus hijos)'), 
                ('proteccion ','Para la Protección (en caso de que no estés tus seres queridos tendrán los recursos)'), 
                )),

                'mount_year':forms.Select(choices=(
                ('',''),
                ('12000 - 30000','Entre $12,000 y $30,000'), 
                ('30000 - 50000','Entre $30,000 y $50,000'), 
                ('50000 - 100000','Entre $50,000 y $100,000'), 
                ('100000 - 999999','Más de $100,000'), 
                )),

                'comments':Textarea(attrs={'cols':80, 'rows':20})
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu Nombre Completo',
        }) 
        self.fields['name_full'].label = 'Nombre Completo'


        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'input-field',
            'type':'datetime-local',
            'placeholder':'Selecciona tu fecha de nacimiento',
        })
        self.fields['date_of_birth'].label = 'Selecciona tu Fecha de Nacimiento'

        self.fields['sex'].widget.attrs.update({
            'class': 'select-field',
        })

        self.fields['sex'].label = 'Selecciona tu Sexo'

        self.fields['marital_status'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['marital_status'].label = 'Selecciona tu Estado Civil'


        self.fields['nationality'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Tu nacionalidad',
        })

        
        self.fields['profession'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Profesión o Ocupación',
        })

        self.fields['postal_code'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Codigo Postal',
        })

        self.fields['address'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Direccion calle, numero, colonia',
        })

        
        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Correo Electronico',
        })

        self.fields['num_phone'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Número de Whatsapp',
        })
        self.fields['num_phone'].label = 'Numero de Whatsapp'

        self.fields['weight'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Peso',
        })
        self.fields['weight'].label = 'Peso'


        self.fields['height'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Estatura',
        })

        self.fields['height'].label = 'Estatura'

        self.fields['smoker'].widget.attrs.update({
            'class': 'input-field',
        })

        self.fields['smoker'].label = '¿En la actualidad fumas? '

        self.fields['sick'].widget.attrs.update({
            'class': 'input-field',
        })

        self.fields['sick'].label = '¿Tienes o has padecido alguna enfermedad o te encuentras en algún tratamiento?'
        
        self.fields['type_insurance'].widget.attrs.update({
            'class': 'select-field',
        })

        self.fields['type_insurance'].label = '¿Qué tipo de seguro te interesa adquirir?'


        self.fields['mount_year'].widget.attrs.update({
            'class': 'select-field',
        })

        self.fields['mount_year'].label = '¿Cuánto estás dispuesto a  invertir anualmente en el seguro?'

        
        self.fields['comments'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['comments'].label = '¿Deseas agregar alguna información adicional?'


class InsuranceCarForm(forms.ModelForm):
    other_vehicle = forms.CharField(label='Especifique', max_length=48,
    widget=Textarea(attrs={'cols':80, 'rows':20}, ))
    class Meta:
        model = InsuranceCar
        fields = '__all__'
        exclude = ['id_car']
        widgets = {

                'vehicle_type':forms.Select(choices=(
                ('',''),
                ('automovil','Automóvil'), 
                ('automovil','Motocicleta'), 
                ('otro','Otros'))
                ),
                
                'description_vehicle':Textarea(attrs={'cols':80, 'rows':20}),

                'coverage_type':forms.Select(choices=(
                ('',''),
                ('amplia','Amplia'), 
                ('limitada','Limitada'), 
                ('responsabilidad civil','Responsabilidad Civil'))
                ),

                'coverage_optional':forms.Select(choices=(
                ('',''),
                ('responsabilidad civil por fallecimiento','Responsabilidad Civil por Fallecimiento'), 
                ('siempre en agencia','Siempre en Agencia'), 
                ('robo parcial','Robo Parcial'),
                ('auto sustituto','Auto Sustituto'),
                ('otro','Otros')
                )),

                'date_of_birth':DateTimeInput(),

                'sex':forms.Select(choices=(('',''),('masculino','Masculino'), 
                ('femenino','Femenino'), 
                ('sin especificar','Sin Especificar'))
                ),

                'comments':Textarea(attrs={'cols':80, 'rows':20})
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['vehicle_type'].widget.attrs.update({
            'class': 'select-field',
        }) 
        self.fields['vehicle_type'].label = 'Selecciona tu tipo de Vehículo'
        
        self.fields['other_vehicle'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['model'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe el modelo de tu vehículo',
        })

        self.fields['description_vehicle'].widget.attrs.update({
            'class': 'input-field',
        })
        self.fields['description_vehicle'].label = 'Escribe la Descripción de tu vehículo (marca, tipo, versión, características especiales, placa o NIV)'

        self.fields['coverage_type'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['coverage_type'].label = 'Selecciona el Tipo de Cobertura'

        self.fields['coverage_optional'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['coverage_optional'].label = 'Selecciona el Tipo de Cobertura Opcional'

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu Nombre Completo',
        }) 

        
        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'input-field',
            'type':'datetime-local',
        })

        self.fields['date_of_birth'].label = 'Selecciona tu Fecha de Nacimiento'
        
        self.fields['sex'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['sex'].label = 'Selecciona tu Sexo'

        self.fields['postal_code'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Codigo Postal',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Correo Electronico',
        })

        self.fields['num_phone'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Número de Whatsapp',
        })
        self.fields['num_phone'].label = 'Numero de Whatsapp'

        
        self.fields['comments'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['comments'].label = '¿Deseas agregar alguna información adicional?'




class InsuranceHouseForm(forms.ModelForm):
    class Meta:
        model = InsuranceHouse
        fields = '__all__'
        exclude = ['id_house']
        widgets = {

                'housing_type':forms.Select(choices=(
                ('',''),
                ('casa unifamiliar o en condominio horizontal','Casa Unifamiliar o en Condominio Horizontal'), 
                ('departamento en condominio','Departamento en Condominio'), 
                ('otro','Otros'))
                ),
                

                'coverage_type':forms.Select(choices=(
                ('',''),
                ('Proteccion total','Protección Total (incendio, fenómenos meteorológicos, sismo y erupción volcánica)'), 
                ('Proteccion Basica','Protección Básica (sólo incendio)'), 
                ('otro','Otros'))
                ),

                'contract_type':forms.Select(choices=(
                ('',''),
                ('dueño o arrendador','Dueño o Arrendador'), 
                ('arrendatario','Arrendatario'),)
                ),

                'comments':Textarea(attrs={'cols':80, 'rows':20})
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['street'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu calle',
        })

        self.fields['number'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu Numero',
        })

        self.fields['suburb'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu Colonia',
        })

        self.fields['postal_code'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu Codigo Postal',
        })

        self.fields['city'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe el Nombre de tu Ciudad',
        })

        self.fields['state'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe el Nombre de tu Estado',
        })


        self.fields['housing_type'].widget.attrs.update({
            'class': 'select-field',
        }) 
        self.fields['housing_type'].label = 'Selecciona tu tipo de Vivienda'

        self.fields['year_house'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe el Año de Construcción',
        })

        self.fields['coverage_type'].widget.attrs.update({
            'class': 'select-field',
        }) 
        self.fields['coverage_type'].label = '¿Qué tipo de cobertura deseas adquirir para tu vivienda? '

        self.fields['house_in_river'].widget.attrs.update({
            'class': 'input-field',
        })
        self.fields['house_in_river'].label = '¿La vivienda se encuentra a menos de 250 metros de un río, canal o laguna?'

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu Nombre Completo',
        }) 

        self.fields['contract_type'].widget.attrs.update({
            'class': 'select-field',
        }) 

        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Correo Electronico',
        })

        self.fields['num_phone'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe tu Número de Whatsapp',
        })
        self.fields['num_phone'].label = 'Numero de Whatsapp'

        
        self.fields['comments'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['comments'].label = '¿Deseas agregar alguna información adicional?'