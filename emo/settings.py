import os
import string

from django.contrib.messages import constants as messages_constants

import dj_database_url
from celery.schedules import crontab
from decouple import Csv, config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config('SECRET_KEY', default=string.ascii_letters)

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',

    'debug_toolbar',
    'crispy_forms',

    'colossus.apps.accounts',
    'colossus.apps.campaigns',
    'colossus.apps.core',
    'colossus.apps.templates',
    'colossus.apps.lists',
    'colossus.apps.notifications',
    'colossus.apps.subscribers',
]

SITE_ID = 1

ROOT_URLCONF = 'colossus.urls'

WSGI_APPLICATION = 'colossus.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'))
    )
}

INTERNAL_IPS = [
    '127.0.0.1',
]


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'colossus.apps.accounts.middleware.UserTimezoneMiddleware',
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'colossus/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'colossus.apps.notifications.context_processors.notifications',
            ],
        },
    },
]

# ==============================================================================
# INTERNATIONALIZATION AND LOCALIZATION SETTINGS
# ==============================================================================

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en-us', 'English'),
    ('pt-br', 'Portuguese'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'colossus/locale'),
)


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'colossus/static'),
]


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media/public')

PRIVATE_MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media/private')


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_SUBJECT_PREFIX = '[Colossus] '

SERVER_EMAIL = config('SERVER_EMAIL', default='root@localhost')

DEFAULT_FROM_EMAIL = config('nisarsasin123@gmail.com', default='webmaster@localhost')

EMAIL_BACKEND = config('django.core.mail.backends.smtp.EmailBackend', default='django.core.mail.backends.smtp.EmailBackend')

EMAIL_HOST = config('smtp.mailgun.org', default='localhost')

EMAIL_PORT = config('587', default='587', cast=int)

EMAIL_HOST_USER = config('postmaster@sandboxaddae8d24cb64b86b9a42d82f2ba8299.mailgun.org', default='root')

EMAIL_HOST_PASSWORD = config('fedd9ffe61697a1406e88556cb034f12-381f2624-16cfb093', default='')

EMAIL_USE_TLS = config('False', default=False, cast=bool)



'''MAIL_DRIVER='smtp'
MAIL_HOST='smtp.yandex.com'
MAIL_PORT='465'
MAIL_USERNAME='d3v-contact'
MAIL_PASSWORD='dvuyrwoepmiqcydd'
MAIL_ENCRYPTION='ssl'
MAIL_FROM_ADDRESS='d3v-contact@yandex.com'
MAIL_FROM_NAME='Support'''

'''MAIL_HOST='smtp.sendgrid.net'
MAIL_PORT='465'
MAIL_USERNAME='apikey'
MAIL_PASSWORD='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'
MAIL_FROM_ADDRESS='sasinnisarga123@gmail.com'
MAIL_FROM_NAME='Sasin'''

# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_USER_MODEL = 'accounts.User'

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

LOGIN_REDIRECT_URL = 'campaigns:campaigns'


# ==============================================================================
# DJANGO CONTRIB APPS SETTINGS
# ==============================================================================

MESSAGE_TAGS = {
    messages_constants.DEBUG: 'alert-dark',
    messages_constants.INFO: 'alert-primary',
    messages_constants.SUCCESS: 'alert-success',
    messages_constants.WARNING: 'alert-warning',
    messages_constants.ERROR: 'alert-danger',
}

if DEBUG:
    MESSAGE_LEVEL = messages_constants.DEBUG
else:
    MESSAGE_LEVEL = messages_constants.INFO

GEOIP_PATH = os.path.join(BASE_DIR, 'bin/GeoLite2')


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='amqp://localhost')

CELERY_BEAT_SCHEDULE = {
    'send-scheduled-campaigns': {
        'task': 'colossus.apps.campaigns.tasks.send_scheduled_campaigns_task',
        'schedule': 60.0
    },
    'clean-lists-hard-bounces': {
        'task': 'colossus.apps.lists.tasks.clean_lists_hard_bounces_task',
        'schedule': crontab(hour=12, minute=0)
    }
}

CELERY_TASK_ALWAYS_EAGER = config('CELERY_TASK_ALWAYS_EAGER', default=True, cast=bool)


# ==============================================================================
# FIRST-PARTY APPS SETTINGS
# ==============================================================================

COLOSSUS_HTTPS_ONLY = config('COLOSSUS_HTTPS_ONLY', default=False, cast=bool)

MAILGUN_API_KEY = config('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', default='')

MAILGUN_API_BASE_URL = config('https://api.mailgun.net/v3/sandboxaddae8d24cb64b86b9a42d82f2ba8299.mailgun.org/', default='')
