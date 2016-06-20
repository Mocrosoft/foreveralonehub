#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Django settings for Viasofie project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w(=vm1bj*^ltsa(!-s06k#@e#e@)h5yzj4@%km_&!2_xgapy*t'

NORECAPTCHA_SITE_KEY = '6LdwqCATAAAAABx3v-fnrR_equMwX8U7PD7Ka9f2'
NORECAPTCHA_SECRET_KEY = '6LfbXCATAAAAACTnQfB-rSSGpMBjENhKHslamNKK'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'groep6mailer@gmail.com'
EMAIL_HOST_PASSWORD = 'Groep6groep'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# GMAIL NEEDS THIS : https://accounts.google.com/displayunlockcaptcha

# Application definition

INSTALLED_APPS = [
    'master',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'inplaceeditform',
    'autofixture',
    'nocaptcha_recaptcha',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]


LANGUAGES = (
    ('en', _('English')),
    ('nl', _('Nederlands')),
    ('fr', _('Français')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

ROOT_URLCONF = 'Viasofie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],              # nu kunnen wij de templates oproepen 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]


WSGI_APPLICATION = 'Viasofie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'viasofie',
        'USER': 'root',
        'PASSWORD': 'Groep6',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'nl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media_cdn/'
DOCUMENTEN_URL = '4685a95f-eebd-401a-9efa-257e1e62124d/' #DO NOT SHARE THIS!!

"""
    Dit is onze development static files directory hierin komen al onze css, js,... 
    Nadat je een bestand toegevoegd (wanneer je volledig klaar ben) moet je deze committen naar uw  
    production static directory (zie STATIC_ROOT ) dit is dan u echte static directory die je gaat gebruiken bij uw live
    website. 
    het sturen van uan development (localhost) naar live server doe je met de volgende commado=>  python manage.py collectstatic 

"""
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  
    os.path.join(BASE_DIR, "media"),                        #ik denk dat dit ook hier moet
]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")         #production  static files

MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")           # dit is voor alle media dat de gebruiker kan uploaden


#INPLACEEDIT

