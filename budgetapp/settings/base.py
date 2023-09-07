"""
Django settings for budgetapp project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
# pylint: disable=wildcard-import unused-wildcard-import

import mimetypes
import os
from pathlib import Path

mimetypes.add_type("text/javascript", ".gz", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DEBUG
DEBUG = False

# https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-ALLOWED_HOSTS
ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/4.0/ref/settings/#site-id
SITE_ID = 1

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "webpack_loader",
    "widget_tweaks",
    "djmoney",
    "guardian",
    "django_htmx",
]

LOCAL_APPS = [
    "budgetapp.apps.users.apps.UsersConfig",
    "budgetapp.apps.budgets.apps.BudgetsConfig",
    "budgetapp.apps.transactions.apps.TransactionsConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

# URLS CONFIG
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#root-urlconf
ROOT_URLCONF = "budgetapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "budgetapp/templates"],
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

# https://docs.djangoproject.com/en/4.0/ref/settings/#wsgi-application
WSGI_APPLICATION = "budgetapp.wsgi.application"

# SET CUSTOM USER MODEL
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting
# -AUTH_USER_MODEL
AUTH_USER_MODEL = "users.User"

# https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-LOGIN_URL
LOGIN_URL = "/users/login/"

# https://docs.djangoproject.com/en/4.0/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "/users/"

# https://docs.djangoproject.com/en/4.0/ref/settings/#logout-redirect-url
LOGOUT_REDIRECT_URL = "/users/login/"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation"
        ".UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation"
        ".NumericPasswordValidator",
    },
]

# Add custom authentication backend
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # default
    "guardian.backends.ObjectPermissionBackend",
)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
TIME_ZONE = "Europe/Bucharest"

# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "ro"

# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = False

# STATIC
# -----------------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "budgetapp/static"]

# MEDIA
# -----------------------------------------------------------------------------
# Mediafiles
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "budgetapp/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Whitenoise configuration
# http://whitenoise.evans.io/en/stable/django.html
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# WEBPACK
# -----------------------------------------------------------------------------
# https://github.com/django-webpack/django-webpack-loader
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "STATS_FILE": os.path.join(BASE_DIR, "webpack/webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}
