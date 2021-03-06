from django import forms
from django.db.models.enums import Choices
from django.forms import widgets
from django.forms import Textarea


from .models import *


class DateTimeInput(forms.DateInput):
    input_type = 'date'


class MedicalExpensesForm(forms.ModelForm):
    class Meta:
        model = MedicalExpenses
        fields = '__all__'
        exclude = ['id_e']
        widgets = {
            'date_of_birth': DateTimeInput(),

            'sex': forms.Select(choices=(('', ''), ('masculino', 'Masculino'),
                                         ('femenino', 'Femenino'),
                                         ('sin especificar', 'Sin Especificar'))
                                ),

            'marital_status': forms.Select(choices=(('', ''), ('solter@', 'Solter@'),
                                                    ('casado', 'Casad@'), ('divorciad@',
                                                                           'Divorciad@'), ('viud@', 'Viud@'),
                                                    ('concubinato',
                                                     'Concubinato')
                                                    )),

            'comments': Textarea(attrs={'cols': 80, 'rows': 20})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu Nombre Completo',
        })
        self.fields['name_full'].label = 'Nombre Completo'

        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'input-field',
            'type': 'datetime-local',
            'placeholder': 'Selecciona tu fecha de nacimiento',
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
            'placeholder': 'Tu nacionalidad',
        })

        self.fields['profession'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Profesi??n o Ocupaci??n',
        })

        self.fields['postal_code'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu C??digo Postal',
        })

        self.fields['address'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Direcci??n calle, n??mero, colonia',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Correo Electr??nico',
        })

        self.fields['num_phone'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu N??mero de Whatsapp',
        })
        self.fields['num_phone'].label = 'N??mero de Whatsapp'

        self.fields['weight'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Peso',
        })
        self.fields['weight'].label = 'Peso'

        self.fields['height'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Estatura',
        })

        self.fields['height'].label = 'Estatura'

        self.fields['parentDiabetes'].widget.attrs.update({
            'class': 'input-field-checkBox',
        })

        self.fields['parentDiabetes'].label = '??Alguno de tus padres, hermanos, t??os o abuelos ha padecido diabetes?'

        self.fields['sick'].widget.attrs.update({
            'class': 'input-field',
        })

        self.fields['sick'].label = '??Tienes o has padecido alguna enfermedad importante o te encuentras en alg??n tratamiento?'

        self.fields['comments'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['comments'].label = '??Deseas agregar alguna informaci??n adicional?'


class LifeInsuranceForm(forms.ModelForm):
    class Meta:
        model = LifeInsurance
        fields = '__all__'
        exclude = ['id_l']
        widgets = {
            'date_of_birth': DateTimeInput(),

            'sex': forms.Select(choices=(('', ''), ('masculino', 'Masculino'),
                                         ('femenino', 'Femenino'),
                                         ('sin especificar', 'Sin Especificar'))
                                ),

            'marital_status': forms.Select(choices=(('', ''), ('solter@', 'Solter@'),
                                                    ('casado', 'Casad@'), ('divorciad@',
                                                                           'Divorciad@'), ('viud@', 'Viud@'),
                                                    ('concubinato',
                                                     'Concubinato')
                                                    )),

            'type_insurance': forms.Select(choices=(('', ''),
                                                    ('ahorro', 'Para el Ahorro (imagina recibir despu??s de 10 a??os los ingresos para cumplir tus sue??os)'),
                                                    ('retiro', 'Para el Retiro (cuando termines de trabajar recibir rentas vitalicias para vivir tu retiro)'),
                                                    ('educaci??n', 'Para la Educaci??n de menores (empieza el proyecto de educaci??n para tus hijos)'),
                                                    ('protecci??n ', 'Para la Protecci??n (en caso de que no est??s tus seres queridos tendr??n los recursos)'),
                                                    )),

            'mount_year': forms.Select(choices=(
                ('', ''),
                ('12000 - 30000', 'Entre $12,000 y $30,000'),
                ('30000 - 50000', 'Entre $30,000 y $50,000'),
                ('50000 - 100000', 'Entre $50,000 y $100,000'),
                ('100000 - 999999', 'M??s de $100,000'),
            )),

            'comments': Textarea(attrs={'cols': 80, 'rows': 20})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu Nombre Completo',
        })
        self.fields['name_full'].label = 'Nombre Completo'

        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'input-field',
            'type': 'datetime-local',
            'placeholder': 'Selecciona tu fecha de nacimiento',
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
            'placeholder': 'Tu nacionalidad',
        })

        self.fields['profession'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Profesi??n o Ocupaci??n',
        })

        self.fields['postal_code'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu C??digo Postal',
        })

        self.fields['address'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Direcci??n calle, n??mero, colonia',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Correo Electr??nico',
        })

        self.fields['num_phone'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu N??mero de Whatsapp',
        })
        self.fields['num_phone'].label = 'N??mero de Whatsapp'

        self.fields['weight'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Peso',
        })
        self.fields['weight'].label = 'Peso'

        self.fields['height'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Estatura',
        })

        self.fields['height'].label = 'Estatura'

        self.fields['smoker'].widget.attrs.update({
            'class': 'input-field-checkBox',
        })
        self.fields['smoker'].label = '??En la actualidad fumas? '

        self.fields['sick'].widget.attrs.update({
            'class': 'input-field-checkBox',
        })
        self.fields['sick'].label = '??Tienes o has padecido alguna enfermedad o te encuentras en alg??n tratamiento?'

        self.fields['type_insurance'].widget.attrs.update({
            'class': 'input-field',
        })
        self.fields['type_insurance'].label = '??Qu?? tipo de seguro te interesa adquirir?'

        self.fields['mount_year'].widget.attrs.update({
            'class': 'select-field',
        })

        self.fields['mount_year'].label = '??Cu??nto est??s dispuesto a  invertir anualmente en el seguro?'

        self.fields['comments'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['comments'].label = '??Deseas agregar alguna informaci??n adicional?'


class InsuranceCarForm(forms.Form):

    vehicle_type = forms.CharField(max_length=48, label='Tipo de Veh??culo',
                                   widget=forms.Select(choices=(
                                       ('', ''),
                                       ('automovil', 'Autom??vil'),
                                       ('automovil', 'Motocicleta'),
                                       ('otro', 'Otros'))))

    other_vehicle = forms.CharField(
        label='Otro Veh??culo',
        max_length=48,
        required=False,
    )

    model = forms.CharField(label='Modelo', max_length=48)
    description_vehicle = forms.CharField(
        label='Descripci??n del Veh??culo', max_length=100, widget=Textarea(attrs={'cols': 80, 'rows': 20}))

    coverage_type = forms.CharField(max_length=48, label='Tipo de Cobertura',
                                    widget=forms.Select(choices=(
                                        ('', ''),
                                        ('amplia', 'Amplia'),
                                        ('limitada', 'Limitada'),
                                        ('responsabilidad civil', 'Responsabilidad Civil'))))

    coverage_optional = forms.MultipleChoiceField(required=False,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  choices=[('responsabilidad civil por fallecimiento',
                                                           'Responsabilidad Civil por Fallecimiento'),
                                                           ('siempre en agencia',
                                                            'Siempre en Agencia'),
                                                           ('robo parcial',
                                                            'Robo Parcial'),
                                                           ('auto sustituto',
                                                            'Auto Sustituto'),
                                                           ('otro', 'Otros')])

    coverage_other = forms.CharField(
        max_length=48,
        required=False,
        label='Otros Descripci??n')

    name_full = forms.CharField(max_length=48, label='Nombre Completo',)
    date_of_birth = forms.CharField(
        max_length=48, label='Nombre Completo', widget=DateTimeInput())

    sex = forms.CharField(max_length=48, label='Sexo', widget=forms.Select(choices=(('', ''), ('masculino', 'Masculino'),
                                                                                    ('femenino',
                                                                                     'Femenino'),
                                                                                    ('sin especificar', 'Sin Especificar'))))

    postal_code = forms.CharField(max_length=10, label='Codigo Postal',)
    email = forms.EmailField(label='Correo Electronico',)
    num_phone = forms.CharField(max_length=10, label='Numero de Whatsapp',)
    comments = forms.CharField(required=False,
                               max_length=300, label='Comentarios Adicionales',
                               widget=Textarea(attrs={'cols': 80, 'rows': 20}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['vehicle_type'].widget.attrs.update({
            'class': 'select-field',
            'id': 'vehicle_type',
        })
        self.fields['vehicle_type'].label = 'Selecciona tu tipo de Veh??culo'

        self.fields['other_vehicle'].widget.attrs.update({
            'class': 'input-field',
            'id': 'other_vehicle_type',
            'placeholder': 'Escribe t?? tipo de tu veh??culo',
        })
        self.fields['model'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe el modelo de t?? veh??culo',
        })

        self.fields['description_vehicle'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['description_vehicle'].label = 'Escribe la Descripci??n de tu veh??culo (marca, tipo, versi??n, caracter??sticas especiales, placa o NIV)'

        self.fields['coverage_type'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['coverage_type'].label = 'Selecciona el Tipo de Cobertura'

        self.fields['coverage_optional'].widget.attrs.update({
            'class': 'multiple-check',
        })

        self.fields['coverage_other'].widget.attrs.update({
            'class': 'input-field',
            'id': 'coverage_other',
            'placeholder': 'Especifica',
        })
        self.fields['coverage_optional'].label = 'Selecciona el Tipos de Coberturas Opcionales:'

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu Nombre Completo',
        })

        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'input-field',
            'type': 'datetime-local',
        })

        self.fields['date_of_birth'].label = 'Selecciona tu Fecha de Nacimiento'

        self.fields['sex'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['sex'].label = 'Selecciona tu Sexo'

        self.fields['postal_code'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu C??digo Postal',
        })

        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Correo Electr??nico',
        })

        self.fields['num_phone'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu N??mero de Whatsapp',
        })
        self.fields['num_phone'].label = 'N??mero de Whatsapp'

        self.fields['comments'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['comments'].label = '??Deseas agregar alguna informaci??n adicional?'


class InsuranceHouseForm(forms.Form):
    street = forms.CharField(max_length=48, label='Calle',)
    number = forms.CharField(max_length=48, label='Numero',)
    suburb = forms.CharField(max_length=48, label='Colonia',)
    postal_code = forms.CharField(max_length=48, label='Codigo Postal')
    city = forms.CharField(max_length=48, label='Ciudad',)
    state = forms.CharField(max_length=48, label='Estado',)
    housing_type = forms.CharField(max_length=48,
                                   widget=forms.Select(choices=(
                                       ('', ''),
                                       ('casa unifamiliar o en condominio horizontal',
                                        'Casa Unifamiliar o en Condominio Horizontal'),
                                       ('departamento en condominio',
                                        'Departamento en Condominio'),
                                       ('otro', 'Otros'))))
    housing_type_other = forms.CharField(
        required=False, max_length=48, label='Otro tipo de vivienda:',)

    year_house = forms.CharField(
        max_length=48, label='A??o de construcci??n de vivienda',)

    coverage_type = forms.CharField(max_length=48,
                                    widget=forms.Select(choices=(
                                        ('', ''),
                                        ('Proteccion total', 'Protecci??n Total (incendio, fen??menos meteorol??gicos, sismo y erupci??n volc??nica)'),
                                        ('Proteccion Basica',
                                         'Protecci??n B??sica (s??lo incendio)'),
                                        ('otro', 'Otros'))))

    coverage_type_other = forms.CharField(
        required=False, max_length=48, label='Otro tipo de cobertura:',)

    house_in_river = forms.BooleanField()
    security_measures = forms.CharField(max_length=100,
                                        widget=forms.Select(
                                            choices=(
                                                ('', ''),
                                                ('Proteccion Perimetral',
                                                 'Protecci??n perimetral)'),
                                                ('Alarma Local', 'Alarma Local'),
                                                ('Alarma Central',
                                                 'Alarma Central'),
                                                ('Control de acceso y vigilancia las 24 horas',
                                                 'Control de acceso y vigilancia las 24 horas')

                                            )))
    name_full = forms.CharField(max_length=48)
    contract_type = forms.CharField(max_length=48,
                                    widget=forms.Select(
                                        choices=(('', ''),
                                                 ('due??o o arrendador',
                                                  'Due??o o Arrendador'),
                                                 ('arrendatario', 'Arrendatario'))))
    email = forms.EmailField(label='Correo Electronico')
    num_phone = forms.CharField(max_length=10, label='Numero de Whatsapp',)
    comments = forms.CharField(required=False,
                               max_length=300, label='Comentarios Adicionales',
                               widget=Textarea(attrs={'cols': 80, 'rows': 20}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['street'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu calle',
        })

        self.fields['number'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu Numero',
        })

        self.fields['suburb'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu Colonia',
        })

        self.fields['postal_code'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu Codigo Postal',
        })

        self.fields['city'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe el Nombre de tu Ciudad',
        })

        self.fields['state'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe el Nombre de tu Estado',
        })

        self.fields['housing_type'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['housing_type'].label = 'Selecciona tu tipo de Vivienda'

        self.fields['housing_type_other'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Especifica',
        })

        self.fields['year_house'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe el A??o de Construcci??n',
        })

        self.fields['coverage_type'].widget.attrs.update({
            'class': 'select-field',
            'id': 'coverage_type',
        })
        self.fields['coverage_type'].label = '??Qu?? tipo de cobertura deseas adquirir para tu vivienda? '

        self.fields['coverage_type_other'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Especifica',
        })

        self.fields['house_in_river'].widget.attrs.update({
            'class': 'input-field',
        })
        self.fields['house_in_river'].label = '??La vivienda se encuentra a menos de 250 metros de un r??o, canal o laguna?'

        self.fields['security_measures'].widget.attrs.update({
            'class': 'select-field',
        })
        self.fields['security_measures'].label = 'Actualmente, ??La vivienda cuenta con alguna de las siguientes medidas de seguridad?'

        self.fields['name_full'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe Tu Nombre Completo',
        })
        self.fields['name_full'].label = 'Nombre Completo'

        self.fields['contract_type'].widget.attrs.update({
            'class': 'select-field',
        })

        self.fields['contract_type'].label = 'Tipo de contratante'

        self.fields['email'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu Correo Electronico',
        })

        self.fields['num_phone'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Escribe tu N??mero de Whatsapp',
        })
        self.fields['num_phone'].label = 'Numero de Whatsapp'

        self.fields['comments'].widget.attrs.update({
            'class': 'input-field input-text-area',
        })
        self.fields['comments'].label = '??Deseas agregar alguna informaci??n adicional?'
