"""
Django settings for curamind project.
"""

from pathlib import Path
from datetime import timedelta
import os
from dotenv import load_dotenv

# -------------------------------------------------
# Load Environment Variables
# -------------------------------------------------
load_dotenv()

# -------------------------------------------------
# Base Directory
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------
# Security
# -------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1").split(",")


# -------------------------------------------------
# Applications
# -------------------------------------------------
INSTALLED_APPS = [
    # Django default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'rest_framework.authtoken',

    # Local apps
    'users',
    'records',
]


# -------------------------------------------------
# Middleware
# -------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -------------------------------------------------
# URLs / WSGI
# -------------------------------------------------
ROOT_URLCONF = 'curamind.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'curamind.wsgi.application'


# -------------------------------------------------
# Database (SQLite for now — PostgreSQL later)
# -------------------------------------------------
# -------------------------------------------------
# Database (SQLite shared for Docker)
# -------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db' / 'db.sqlite3',
    }
}
# -------------------------------------------------
# Password Validation
# -------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------------------------------------
# Internationalization
# -------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------
# Static Files
# -------------------------------------------------
STATIC_URL = '/static/'


# -------------------------------------------------
# Media Files
# -------------------------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# -------------------------------------------------
# Custom User Model
# -------------------------------------------------
AUTH_USER_MODEL = 'users.User'


# -------------------------------------------------
# REST Framework Configuration
# -------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# -------------------------------------------------
# JWT Configuration
# -------------------------------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


# -------------------------------------------------
# Default Primary Key
# -------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# -------------------------------------------------
# Celery Configuration (Docker Compatible)
# -------------------------------------------------
CELERY_BROKER_URL = os.getenv(
    "CELERY_BROKER_URL", "redis://redis:6379/0"
)

CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND", "redis://redis:6379/0"
)

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

