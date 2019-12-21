import os
import dj_database_url
from dotenv import load_dotenv
from environs import Env


load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
secret_key = os.getenv('SECRET_KEY')
engine = os.getenv('ENGINE_DB')
host = os.getenv("SECRET_HOST")
port = os.getenv("SECRET_PORT")
name = os.getenv("SECRET_NAME ")


# DATABASES = {
#     'default': {
#         'ENGINE':engine,
#         'HOST': host,
#         'PORT': port,
#         'NAME': name,
#         'USER': username,
#         'PASSWORD': password,
#     }
# }
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
    }
}



INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = bool(os.environ.get('DJANGO_DEBUG',True))
print(DEBUG)


ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DATABASES['default'] = dj_database_url.config(conn_max_age=500)

