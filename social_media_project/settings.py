"""
Django settings for social_media_project project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import sys
import dj_database_url
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['261e-2a09-bac1-6f20-1060-00-1f1-20b.ngrok-free.app','8000-kay13051976-thailandgui-jfkilhjpyib.ws-eu107.gitpod.io',
                 'thailand-guiding-light-2fb0b0e33db8.herokuapp.com',
                 'thailand-guiding-light.herokuapp.com', 
                 'localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'cloudinary_storage',
    'cloudinary',
    'home_app',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'social_media_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'social_media_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# postgres://kqlgwsfz:PELGcwjjMrkuyEzZkzfvzUNDyXSgfF4N@snuffleupagus.db.elephantsql.com/kqlgwsfz
# postgres://rmitzrwu:AvsjvRMu9UUiazfOHuaYKy79m6adNK6v@tiny.db.elephantsql.com/rmitzrwu
# postgres://dyowxatm:BzwENgJEMNvooZAO4OoGR8VVodlXqxdd@arjuna.db.elephantsql.com/dyowxatm
# postgres://diyosqfn:EPOT-yiDsxg6SVbymcDcDsATSCdK8nR_@manny.db.elephantsql.com/diyosqfn
# postgres://chfbxfsq:s-_OsitArsivt6bTBZEVipX1iAapQwwG@rogue.db.elephantsql.com/chfbxfsq

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    
}

# Use SQLite for testing
if 'test' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['NAME'] = BASE_DIR / "db.sqlite3"

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR 
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


AUTHENTICATION_BACKENDS = [
    # ...
    'allauth.account.auth_backends.AuthenticationBackend',
    # ...
]


# Enable Django Allauth
SITE_ID = 1  # You may need to change this based on your site configuration
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'


CSRF_TRUSTED_ORIGINS=["http://127.0.0.1:8000","https://8000-kay13051976-thailandgui-jfkilhjpyib.ws-eu107.gitpod.io"]


ACCOUNT_FORMS = {'signup': 'home_app.forms.CustomSignupForm'}


CLOUDINARY_STORAGE = {
             'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
             'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
             'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET')
            }
DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'
