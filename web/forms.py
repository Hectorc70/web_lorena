from django import forms

from .models import LifeInsurance

class LifeInsuranceForm(forms.ModelForm):

    class Meta:
        model = LifeInsurance
        fields = '__all__'
    

