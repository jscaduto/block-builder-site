"""
Django settings for blockbuildersite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2!##h$^l*8(eki2i=d4qj+6s5hw0=17f3+qi&d%ks9c04%x62z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blockbuildersite',
    'blockbuilder',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blockbuildersite.urls'

WSGI_APPLICATION = 'blockbuildersite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = '/opt/djangoprojects/static/'
STATIC_URL = '/static/'

BLOCK_SETS = {
    'ED_ELETHA_BLOCKS': [
        'OSBHML',
        'AECRGO',
        'PRAJMF',
        'SDRUPY',
        'POYGGV',
        'BCAHSE',
        'HILNTA',
        'REQNLS',
        'LXWINT',
        'HSEOTV',
        'WDTEIR',
        'EANMRK',
        'AYSEGF',
        'SCANOB',
        'URIFDL',
        'LGKYZ4',
    ],
    'ROGER_MOLLY_BLOCKS': [
        'MBLHSN',
        'CAGOTE',
        'NRPFAJ',
        'SUTDPR',
        'VGIPOY',
        'ECSABH',
        'LHAINT',
        'QRSNEO',
        'TWHMLX',
        'HTOESV',
        'EIDTWR',
        'AKREMN',
        'GEFYHA',
        'BONACS',
        'FLURDI',
        'O4EYKZ',
    ]
}