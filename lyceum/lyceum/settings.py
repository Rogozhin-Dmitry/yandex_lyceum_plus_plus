from pathlib import Path
from os import path

import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "debug_toolbar",
    "homepage.apps.HomepageConfig",
    "catalog.apps.CatalogConfig",
    "about.apps.AboutConfig",
    "users.apps.UsersConfig",
    "rating.apps.RatingConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    'widget_tweaks',
    'sorl.thumbnail',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]

ROOT_URLCONF = "lyceum.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "lyceum.wsgi.application"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        + "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        + "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        + "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        + "NumericPasswordValidator",
    },
]

INTERNAL_IPS = [
    "127.0.0.1",
]

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'send_emails'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profile'

# Internationalization

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    path.join(BASE_DIR, "lyceum_static"),
]

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = ["users.backends.EmailBackend"]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
