# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def ABS_PATH(*args):
    return os.path.join(ROOT_DIR, *args)


SITE_ID = 1

LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('it', 'Italian'),
    ('hr', 'Croatian'),
]

DEBUG = True
TEMPLATE_DEBUG = True

FIXTURE_DIRS = (
    ABS_PATH('tests', 'fixtures'),
)

USE_TZ = True

ROOT_URLCONF = 'tests.urls'

SECRET_KEY = 'secretkey'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'cms',
    'menus',
    'treebeard',
    'mptt',
    'easy_thumbnails',
    'filer',
    'djangocms_text_ckeditor',
    'parler',
    'blogit',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


# blogit
BLOGIT_SINGLE_APPHOOK = True
