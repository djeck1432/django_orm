import os
from dotenv import load_dotenv
from environs import Env

env = Env()
env.read_env()

load_dotenv()
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
secret_key = os.getenv('SECRET_KEY')



DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'HOST': db_host,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_username,
        'PASSWORD':db_password,
    }
}



INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key


DEBUG = env.bool('DEBUG')


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
