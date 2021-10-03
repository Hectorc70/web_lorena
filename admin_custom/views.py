
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from admin_custom.utils import FileExcel

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
		'car': autos,
		'house': house,
	})

def download_medical(request):
	#response = HttpResponse(content_type='application/ms-excel')
	#response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'


	columns = [
			'Nombre', 
			'Fecha de Nac', 
			'Sexo 3', 'Estado Civil', 
			'Nacionalidad',
			'Profesion',
			'CP',
			'Calle',
			'Email',
			'Whatssap',
			'Altura',
			'Peso',
			'Pariente Con Diabetes',
			'Enfermedad',
			'Comentarios'
			]
	excel = FileExcel(
		name_file='GastosMedicos',
		shet_name='Hoja1'
	)
	data =  MedicalExpenses.objects.all()
	excel.write_file_medical(columns, data)

	return excel.response

