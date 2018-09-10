"""
Django settings for sven project.

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
SECRET_KEY = 'h-qll9se-6*w7h7%6owg4nv=gp%q67tl^b^sev7p6k*%c#_hx3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

# Application definition

INSTALLED_APPS = (
    'pipeline',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

#    'sven.apps.dashboard',
#    'sven.apps.configuration',
    'sven.apps.monitor',

#    'sven.apps.activity',
#    'sven.apps.sensors',

    'sven.libs.display',
    'sven.libs.management'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sven.urls'

WSGI_APPLICATION = 'sven.wsgi.application'

#STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sven',                                     # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'sven',
        'PASSWORD': 'sven',
        'HOST': '10.10.0.224',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    },
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sven.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'PST8PDT'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

STATICFILES_DIRS = (
  os.path.join( SITE_ROOT, 'static/' ),
)

import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s %(levelname)s %(message)s',
    filename = '/tmp/djangoLog.log',)

PIPELINE_JS = {
    'core': {
        'source_filenames': (
            'js/setup.js',
            'js/developr.accordions.js',
            'js/developr.auto-resizing.js',
            'js/developr.input.js',
            'js/developr.message.js',
            'js/developr.modal.js',
            'js/developr.navigable.js',
            'js/developr.collapsible.js',
            'js/developr.notify.js',
            'js/developr.scroll.js',
            'js/developr.progress-slider.js',
            'js/developr.tooltip.js',
            'js/developr.confirm.js',
            'js/developr.content-panel.js',
            'js/developr.agenda.js',
            'js/developr.table.js',
            'js/developr.tabs.js',
            'js/libs/formValidator/languages/jquery.validationEngine-en.js',
            'js/libs/formValidator/jquery.validationEngine.js',
            'js/libs/glDatePicker/glDatePicker.min.js',
            'js/libs/jquery.ba-hashchange.min.js',
            'js/libs/jquery.tablesorter.min.js',
            'js/libs/DataTables/jquery.dataTables.min.js',
        ),
        'output_filename': 'js/core_combined.js',
    }
}

PIPELINE_ENABLED = False
