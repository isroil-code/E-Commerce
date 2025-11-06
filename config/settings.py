
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Keep a sane default for local development but allow overriding via env var in Docker/production
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    'django-insecure-km4059xz5_m)jrbi*pgqg=hw!mgf1yw-t=mh73icqm^zvz3nfp'
)

# DEBUG should be explicitly set via env (1/true/yes -> True). Default to False in containers.
_DEBUG_ENV = os.environ.get("DEBUG", "0")
DEBUG = _DEBUG_ENV in ("1", "true", "True", "yes")

# Hosts allowed (comma-separated in DJANGO_ALLOWED_HOSTS). Default to localhost for dev.
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "127.0.0.1").split(",")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'cart.apps.CartConfig',
    'products.apps.ProductsConfig',
    'main',
    'rest_framework',
   
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.ContextProcessors.general_info'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



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

# DATABASE configuration: use sqlite3 by default, but allow switching via env vars (e.g. postgres)
DATABASE_ENGINE = os.getenv('DATABASE_ENGINE', 'sqlite3')
if DATABASE_ENGINE == 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # Expected DATABASE_ENGINE values: 'postgresql', 'mysql', etc.
    DATABASES = {
        'default': {
            'ENGINE': f"django.db.backends.{DATABASE_ENGINE}",
            'NAME': os.getenv('DATABASE_NAME', 'savdo'),
            'USER': os.getenv('DATABASE_USERNAME', 'postgres'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD', 'postgres'),
            'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
            'PORT': os.getenv('DATABASE_PORT', '5432'),
        }
    }


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




STATIC_URL = 'static/'
# Where `collectstatic` will collect files for production/static serving
STATIC_ROOT = BASE_DIR / 'staticfiles'


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
    
LOGOUT_REDIRECT_URL = '/accounts/login/' 


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
