
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from web.models import *


# Create your views here.

@csrf_protect
def login_admin(request):
    """vista para poder ingresar a la pagina"""

    if request.method == 'POST':
        user = request.POST.get('user')
        psword = request.POST.get('password')

        usuario = authenticate(username=user, password=psword)
        if usuario:
            login(request, usuario)

            messages.success(request, 'A ingresado correctamente')
            return redirect('admin-c:admin')

        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html')

    return render(request, 'login.html')


@login_required()
def logoutAdmin(request):
    logout(request)
    messages.success(request, "Sesion Finalizada")

    return redirect('admin-c:login')


def view_admin(request):
    medical = MedicalExpenses.objects.all()
    life = LifeInsurance.objects.all()
    autos = InsuranceCar.objects.all()
    house = InsuranceHouse.objects.all()

    return render(request, 'admin.html', {
        'medical': medical,
        'life': life,
        'autos': autos,
        'house': house,
    })
