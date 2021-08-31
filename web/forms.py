from django import forms
from django.forms import widgets
from django.forms import Textarea

from .models import LifeInsurance


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

        self.fields['sex'].widget.attrs.update({
            'class': 'select-field',
            'placeholder':'Selecciona tu Sexo',
        })

        self.fields['marital_status'].widget.attrs.update({
            'class': 'select-field',
            'placeholder':'Selecciona tu Estado Civil',
        })


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
            'class': 'input-field',
        })
        self.fields['comments'].label = '¿Deseas agregar alguna información adicional?'


