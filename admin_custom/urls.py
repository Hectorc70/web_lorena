
from django.urls import path

from admin_custom.views import *

app_name = 'admin_custom'

urlpatterns = [
    path('', login_admin, name='login'),
    path('home-admin/', view_admin, name='admin'),
    path('logout/', logoutAdmin, name="logout"),

    path('download-medical/', download_medical, name='download_medical'),
    path('download-life/', download_life, name='download_life'),
    path('download-car/', download_car, name='download_car'),
    path('download-house/', download_house, name='download_house'),
]
