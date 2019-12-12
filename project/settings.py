import os
from dotenv import load_dotenv
from environs import Env


load_dotenv()
<<<<<<< HEAD
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
secret_key = os.getenv('SECRET_KEY')
engine = os.getenv('ENGINE_DB')
host = os.getenv("SECKRET_HOST")
port = os.getenv("SECRET_PORT")
name = os.getenv("SECRET_NAME ")
=======
username = os.getenv('user')
password = os.getenv('password')
>>>>>>> 8ea26a016cdb0e163b7568b1f8c48651ff25e7e0

DATABASES = {
    'default': {
        'ENGINE':engine,
        'HOST': host,
        'PORT': port,
        'NAME': name,
        'USER': username,
        'PASSWORD': password,
    }
}

INSTALLED_APPS = ['datacenter']

<<<<<<< HEAD
SECRET_KEY = secret_key
env = Env()
env.read_env()

DEBUG = env('false')
=======
SECRET_KEY = 'REPLACE_ME'
env = Env()
env.read_env()

DEBUG = env('True')
>>>>>>> 8ea26a016cdb0e163b7568b1f8c48651ff25e7e0

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
