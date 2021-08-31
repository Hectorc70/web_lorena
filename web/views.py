from django.shortcuts import render

from .models import *
from .forms import *
# Create your views here.

def view_home(request):  
    form_life_insurance = LifeInsuranceForm() 
    form_insurance_car = InsuranceCarForm() 

    return render(request, 'index.html', {'form_life_insurance':form_life_insurance, 'form_insurance_car':form_insurance_car})