from django.shortcuts import render

from .models import LifeInsurance
from .forms import LifeInsuranceForm
# Create your views here.

def view_home(request):  
    form_life_insurance = LifeInsuranceForm() 
    return render(request, 'index.html', {'form_life_insurance':form_life_insurance})