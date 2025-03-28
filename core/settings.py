from pathlib import Path
import os
from os import getenv
from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-futhsy75_1@17l&max_a9d#b)k597*#mp9aj0(pdg9f$t2hsrb'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'blog.apps.BlogConfig',
    'service.apps.ServiceConfig',
    'video.apps.VideoConfig',
    'contact.apps.ContactConfig',
    'admin_interface',
    'colorfield',
    'rest_framework',
    'ckeditor',
    # 'jazzmin',
    # 'semantic_admin',
    # 'semantic_forms',
    # 'unfold',
    # 'unfold.contrib.filters',
    # 'unfold.contrib.forms',
    # 'unfold.contrib.inlines',
    # 'unfold.contrib.import_export',
    # 'unfold.contrib.guardian',
    'rosetta',
    'modeltranslation',
    'django.contrib.admin',
    'django_cleanup.apps.CleanupConfig',
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'base.middleware.TranslationMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'




# if not DEBUG:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': getenv('POSTGRES_DB'),
#             'USER': getenv('POSTGRES_USER'),
#             'PASSWORD': getenv('POSTGRES_PASSWORD'),
#             'HOST': getenv('POSTGRES_HOST'),
#             'PORT': 5432,
#         }
# }



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


LANGUAGE_CODE = 'tr'

USE_TZ = True

USE_L10N = True

USE_I18N = True

TIME_ZONE = 'Asia/Istanbul'

LANGUAGES = (
    ('tr', 'Turkish'),
    ('ar', 'Arabic'),
    ('kk', 'Kurdish'),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'tr'
MODELTRANSLATION_LANGUAGES = ['tr', 'ar', 'kk']
MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'default': (),
}


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

API_KEY = "AIzaSyDfkOf5ukZEt5sGsXHg7qh6iXBd3L7pXIM"
CHANNEL_ID = "UCn6c3M9iD_-i0twEX0r2V0g"

EMAIL_BACKEND = getenv('EMAIL_BACKEND')
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = getenv('EMAIL_PORT')
EMAIL_USE_TLS = getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')