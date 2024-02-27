# 배포용 환경

from .base import *

def read_secret(secret_name): #secrete_name을 받아서, 해당 이름을 가진 secrete를 불러와라
    file = open('/run/secrets/' + secret_name) #open 함수를 사용하여 /run/secrets/ 경로와 secret_name을 결합하여 파일을 염
    secret = file.read()
    secret = secret.rstrip().lstrip() #읽어온 시크릿 문자열의 양쪽 공백을 제거합니다.
    file.close()
    return secret

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# env라는 변수 안에, .env파일 안의 변수들이 할당이 됨
# reading .env file
environ.Env.read_env(
    env_file = os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY') #.env파일 안에서 SECRET_KEY를 읽어옴

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*'] #모든 호스트에 대해 허용한다는 세팅

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql", #mariadb를 쓰지만 mysql이라 씀(구성은 거의 같음)
        "NAME": "django",
        "USER": "django",
        "PASSWORD": read_secret('MYSQL_PASSWORD'),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}