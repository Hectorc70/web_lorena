from django import forms
from django.forms import widgets

from .models import LifeInsurance


class DateTimeInput(forms.DateInput):
    input_type = 'date'

class LifeInsuranceForm(forms.ModelForm):
    field = forms.ChoiceField(choices=(('Masculino','masculino'), ('Femenino','femenino'), ('Sin Especificar','sin especificar')))
    class Meta:
        model = LifeInsurance
        fields = '__all__'
        exclude = ['id_l']
        widgets = {
                'date_of_birth':DateTimeInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder':'Escribe Tu Nombre Completo',
        })

        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'input-field',
            'type':'datetime-local',
            'placeholder':'Selecciona tu fecha de nacimiento',
        })

        self.fields['name_full'].label = 'Nombre Completo'


