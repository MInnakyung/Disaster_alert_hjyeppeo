"""
Django settings for jaenani project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9%mwuutvcd$ih#6_id8&y*ddxv*sf4^v_v5!xc-8+rt=433b1m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
        'http://115.85.183.131',
        ]
# Application definition

INSTALLED_APPS = [
    'django_cleanup.apps.CleanupConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'boards',
    'corsheaders',
    'sslserver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'jaenani.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jaenani.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 미디어 url
MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/'

# admin 수정
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# session
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
PROTOCOL = 'https'
HOSTNAME = '115.85.183.131:8000'
# email
# 메일을 보내는 호스트 서버
EMAIL_HOST = 'smtp.gmail.com'

# ENAIL_HOST에 정의된 SMTP 서버가 사용하는 포트 (587: TLS/STARTTLS용 포트)
EMAIL_PORT = '587'

#  발신할 이메일 주소 '~@gmail.com'
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")

# 발신할 이메일 비밀번호 (2단계 인증일경우 앱 비밀번호)
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# TLS 보안 방법 (SMPT 서버와 통신할 떄 TLS (secure) connection 을 사용할지 말지 여부)
EMAIL_USE_TLS = True

# 사이트와 관련한 자동응답을 받을 이메일 주소
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
