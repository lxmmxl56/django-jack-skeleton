"""
Django settings for jack project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import socket
import sys
from configparser import RawConfigParser

from django.contrib import messages
from django.urls import reverse_lazy

SITE_ID = 1

# Constants for DJANGO_HOST
PROD = 'prod'
DEV = 'dev'
LOCAL = 'local'

if socket.gethostname().startswith('prodHost'):  # pragma: no cover
    DJANGO_HOST = PROD
elif socket.gethostname().startswith('stageHost'):  # pragma: no cover
    DJANGO_HOST = DEV
else:
    DJANGO_HOST = LOCAL

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = RawConfigParser()
config.read(os.path.join(BASE_DIR, 'jack/config.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('keys', 'secret')

# SECURITY WARNING: don't run with debug turned on in production!
if PROD == DJANGO_HOST:  # pragma: no cover
  DEBUG = False
  SECURE_HSTS_SECONDS = 60
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  SECURE_SSL_REDIRECT = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
else:
  DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

ADMINS = (
    ('jack.admin', 'jack-admin@email.com'),
)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mailer',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'jack/templates/')],
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

WSGI_APPLICATION = 'jack.wsgi.application'

# Database
if LOCAL == DJANGO_HOST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'data/db.sqlite3'),
        }
    }
else:  # pragma: no cover
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'jack',
            'USER': 'jackuser',
            'PASSWORD': config.get('keys', 'database'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Authentication
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')
# LOGIN_REDIRECT_URL = reverse_lazy('index')

# Password validation
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
LANGUAGE_CODE = 'en'
from django.utils.translation import gettext_lazy as _
LANGUAGES = [
  ('en', _('English')),
  ('ja', _('Japanese')),
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'jack/locale/'),
]
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

FORMAT_MODULE_PATH = [
    'jack.formats',
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'html/static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'jack/static/'),
]

# Logging configuration
DEBUG_LOGGER = "debug_logger"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/logs/debug.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['console', ],
            'propagate': True,
        },
        'debug_logger': {
            'handlers': ['debug_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

if DJANGO_HOST == LOCAL:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:  # pragma: no cover
    EMAIL_BACKEND = 'mailer.backend.DbBackend'

EMAIL_HOST = 'mx.email.com'
EMAIL_HOST_USER = 'jack-admin@email.com'
EMAIL_HOST_PASSWORD = config.get('keys', 'email')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'django-jack@email.com'
SERVER_EMAIL = 'jack-admin@email.com'

# Filesystem path to the directory that will hold user generated files
# media will be authenticated and delivered via the restricted_media URL
# MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'html/media')

# Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'account.authentication.EmailAuthBackend',
)

# Messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

TESTING = 'test' in sys.argv

if TESTING:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'data/db.sqlite3'),
        }
    }
