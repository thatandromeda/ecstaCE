"""
Django settings for ecstaCE project.

Generated by 'django-admin startproject' using Django 1.8.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# ------------------------------------------------------------------------------
# ------------------------> core django configurations <------------------------
# ------------------------------------------------------------------------------

# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'crispy_forms',
)

LOCAL_APPS = (
    'ecstaCE.courses',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


# DEBUG
# ------------------------------------------------------------------------------

# By setting this an an environment variable, it is easy to switch debug on in
# servers to do a quick test.
# DEBUG SHOULD BE FALSE ON PRODUCTION for security reasons. This means
# DJANGO_DEBUG must be *unset* - anything set will evaluate to True.

DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecstace',
        'USER': os.environ.get('DJANGO_DB_USER', None),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', None),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------

# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# In production, this list should contain the URL of the server and nothing
# else, for security reasons. For local testing '*' is OK.
ALLOWED_HOSTS = []

ROOT_URLCONF = 'ecstaCE.urls'

WSGI_APPLICATION = 'ecstaCE.wsgi.application'

SITE_ID = 1


# INTERNATIONALIZATION CONFIGURATION
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
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


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'collectedstatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'brief': {
            'format': '%(asctime)s %(levelname)s %(name)s[%(funcName)s]: %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'ecstaCE.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter': 'brief',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    }
}


# ------------------------------------------------------------------------------
# -----------------> third-party and ecstaCE configurations <-------------------
# ------------------------------------------------------------------------------

CRISPY_TEMPLATE_PACK = 'bootstrap3'
