# 로컬 개발 환경

from .base import *

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
SECRET_KEY = env('SECRET_KEY') #.env파일 안에서 SECRET_KEY를 읽어옴

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] #모든 호스트에 대해 허용한다는 세팅

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}