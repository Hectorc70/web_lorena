from web.utils import get_all_coverage_optionals
from django.contrib import messages
from django.shortcuts import render

from .models import *
from .forms import *
# Create your views here.


def view_home(request):
    form_medical_expenses = MedicalExpensesForm()
    form_life_insurance = LifeInsuranceForm()
    form_insurance_car = InsuranceCarForm()
    form_insurance_house = InsuranceHouseForm()

    form_life = LifeInsuranceForm(request.POST)
    form_medical = MedicalExpensesForm(request.POST)
    form_car = InsuranceCarForm(request.POST)
    form_house = InsuranceHouseForm(request.POST)

    if request.method == 'POST' and form_medical.is_valid():
        name_full = form_medical.cleaned_data.get('name_full')
        date_of_birth = form_medical.cleaned_data.get('date_of_birth')
        sex = form_medical.cleaned_data.get('sex')
        marital_status = form_medical.cleaned_data.get('marital_status')
        nationality = form_medical.cleaned_data.get('nationality')
        profession = form_medical.cleaned_data.get('profession')
        postal_code = form_medical.cleaned_data.get('postal_code')
        address = form_medical.cleaned_data.get('address')
        email = form_medical.cleaned_data.get('email')
        num_phone = form_medical.cleaned_data.get('num_phone')
        weight = form_medical.cleaned_data.get('weight')
        height = form_medical.cleaned_data.get('height')
        parentDiabetes = form_medical.cleaned_data.get('parentDiabetes')
        sick = form_medical.cleaned_data.get('sick')
        comments = form_medical.cleaned_data.get('comments')
        

        form = MedicalExpenses(
            name_full = name_full,
            date_of_birth = date_of_birth,
            sex = sex,
            marital_status = marital_status,
            nationality = nationality,
            profession = profession,
            postal_code = postal_code,
            address = address,
            email = email,
            num_phone = num_phone,
            weight = weight,
            height = height,
            parentDiabetes = parentDiabetes,
            sick = sick,
            comments = comments,)
        
        try:
            form.save()
            messages.success(
                request, 'Informacion enviada sera contactado en breve')
        except:
            messages.error(
                request, 'Error al guardar Datos')

    elif request.method == 'POST' and form_life.is_valid():

        name_full = form_life.cleaned_data.get('name_full')
        date_of_birth = form_life.cleaned_data.get('date_of_birth')
        sex = form_life.cleaned_data.get('sex')
        marital_status = form_life.cleaned_data.get('marital_status')
        nationality = form_life.cleaned_data.get('nationality')
        profession = form_life.cleaned_data.get('profession')
        postal_code = form_life.cleaned_data.get('postal_code')
        address = form_life.cleaned_data.get('address')
        email = form_life.cleaned_data.get('email')
        num_phone = form_life.cleaned_data.get('num_phone')
        weight = form_life.cleaned_data.get('weight')
        height = form_life.cleaned_data.get('height')
        smoker = form_life.cleaned_data.get('smoker')
        sick = form_life.cleaned_data.get('sick')
        type_insurance = form_life.cleaned_data.get('type_insurance')
        mount_year = form_life.cleaned_data.get('mount_year')
        comments = form_life.cleaned_data.get('comments')

        form = LifeInsurance(
            name_full=name_full,
            date_of_birth=date_of_birth,
            sex=sex,
            marital_status=marital_status,
            nationality=nationality,
            profession=profession,
            postal_code=postal_code,
            address=address,
            email=email,
            num_phone=num_phone,
            weight=weight,
            height=height,
            smoker=smoker,
            sick=sick,
            type_insurance=type_insurance,
            mount_year=mount_year,
            comments=comments,
        )
        try:
            form.save()
            messages.success(
                request, 'Informacion enviada sera contactado en breve')
        except:
            messages.error(
                request, 'Error al guardar Datos')

    elif request.method == 'POST' and form_car.is_valid():
        vehicle_type = form_car.cleaned_data.get('vehicle_type')
        other_vehicle_type = form_car.cleaned_data.get('other_vehicle')
        model = form_car.cleaned_data.get('model')
        description_vehicle = form_car.cleaned_data.get('description_vehicle')
        coverage_type = form_car.cleaned_data.get('coverage_type')
        coverage_optional = form_car.cleaned_data.get('coverage_optional')
        coverage_other = form_car.cleaned_data.get('coverage_other')
        
        name_full = form_car.cleaned_data.get('name_full')
        date_of_birth = form_car.cleaned_data.get('date_of_birth')
        postal_code = form_car.cleaned_data.get('postal_code')
        email = form_car.cleaned_data.get('email')
        num_phone = form_car.cleaned_data.get('num_phone')
        comments = form_car.cleaned_data.get('comments')

        
        
        if vehicle_type == 'otro':
            vehicle_type = other_vehicle_type
        
        if 'otro' in coverage_optional:
            coverage_optional.remove('otro')
            coverage_optional.append(coverage_other)
        
        form = InsuranceCar(
            vehicle_type=vehicle_type,
            model=model,
            description_vehicle=description_vehicle,
            coverage_type=coverage_type,
            coverage_optional = coverage_optional,
            name_full=name_full,
            date_of_birth=date_of_birth,
            postal_code=postal_code,
            email=email,
            num_phone=num_phone,
            comments=comments,
        )
        try:
            form.save()
            messages.success(
                request, 'Informacion enviada sera contactado en breve')
        except:
            messages.error(
                request, 'Error al guardar Datos')

        
    elif request.method == 'POST' and form_house.is_valid():
        street = form_house.cleaned_data.get('street') 
        number = form_house.cleaned_data.get('number') 
        suburb = form_house.cleaned_data.get('suburb') 
        postal_code = form_house.cleaned_data.get('postal_code') 
        city = form_house.cleaned_data.get('city') 
        state = form_house.cleaned_data.get('state') 
        housing_type = form_house.cleaned_data.get('housing_type') 
        housing_type_other = form_house.cleaned_data.get('housing_type_other') 
        year_house = form_house.cleaned_data.get('year_house') 
        coverage_type = form_house.cleaned_data.get('coverage_type') 
        coverage_type_other = form_house.cleaned_data.get('coverage_type_other') 
        house_in_river = form_house.cleaned_data.get('house_in_river') 
        security_measures = form_house.cleaned_data.get('security_measures') 
        name_full = form_house.cleaned_data.get('name_full') 
        contract_type = form_house.cleaned_data.get('contract_type') 
        email = form_house.cleaned_data.get('email') 
        num_phone = form_house.cleaned_data.get('num_phone') 
        comments = form_house.cleaned_data.get('comments') 

        import pdb; pdb.set_trace()
        if housing_type == 'otro':
            housing_type = housing_type_other
        
        if coverage_type == 'otro':
            coverage_type = coverage_type_other
        

        form = InsuranceHouse(
            street = street,
            number = number,
            suburb = suburb,
            postal_code = postal_code,
            city = city,
            state = state,
            housing_type = housing_type,
            year_house = year_house,
            coverage_type = coverage_type,
            house_in_river = house_in_river,
            security_measures = security_measures,
            name_full = name_full,
            contract_type = contract_type,
            email = email,
            num_phone = num_phone,
            comments = comments,
        )

        try:
            form.save()
            messages.success(
                request, 'Informacion enviada sera contactado en breve')
        except:
            messages.error(
                request, 'Error al guardar Datos')




    return render(request, 'index.html', {
        'form_medical_expenses':form_medical_expenses,
        'form_life_insurance': form_life_insurance, 
        'form_insurance_car': form_insurance_car, 
        'form_insurance_house': form_insurance_house})



def view_creditos(request):

    return render(request, 'creditos.html',{})


