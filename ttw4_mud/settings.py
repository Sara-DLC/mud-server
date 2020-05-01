"""
Django settings for ttw4_mud project.

Generated by "django-admin startproject" using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from decouple import config, Csv
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

############################################################
#   SECURITY
############################################################

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

CORS_ORIGIN_ALLOW_ALL = config("CORS_ORIGIN_ALLOW_ALL", cast=bool, default=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=False)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

############################################################
#   APPLICATION DEFINITION
############################################################

INSTALLED_APPS = [
    # project's apps
    "api",
    "accounts",
    "adventure",

    # tools
    "corsheaders",
    "whitenoise",

    # rest
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
    "rest_auth.registration",
    "allauth",
    "allauth.account",

    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "ttw4_mud.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ttw4_mud.wsgi.application"

# the following makes `rest_auth` work?

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

############################################################
#   DATABASE
#   https://docs.djangoproject.com/en/3.0/ref/settings/#databases
############################################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

############################################################
#   AUTH
#   https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
############################################################

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

############################################################
#   INTERNATIONALIZATION
#   https://docs.djangoproject.com/en/3.0/topics/i18n/
############################################################

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True

############################################################
#   STATIC FILES (CSS, JavaScript, Images)
#   https://docs.djangoproject.com/en/3.0/howto/static-files/
############################################################

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

############################################################

# Activate Django-Heroku.
django_heroku.settings(locals())
