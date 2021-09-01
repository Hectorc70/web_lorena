import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser()
config.read("config.ini")
tipo = config['DEV']

ALLOWED_HOSTS = ['192.168.0.194', '127.0.0.1']
SECRET_KEY = tipo['SECRET_KEY']
DEBUG = True

DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.mysql',
            'NAME':tipo['DB_NAME'],
            'USER':tipo['DB_USER'],
            'PASSWORD': tipo['DB_PASSWORD'],
            'HOST': tipo['DB_HOST'],
            'PORT': tipo['DB_PORT'],
        }
}