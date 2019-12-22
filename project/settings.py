import os
from dotenv import load_dotenv


load_dotenv()
username = os.getenv('USERNAME_DB')
password = os.getenv('PASSWORD_DB')
secret_key = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': username,
        'PASSWORD': password,
    }
}



INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = bool(os.environ.get('DJANGO_DEBUG',default=False))


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
