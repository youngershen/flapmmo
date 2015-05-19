# -*- coding:utf-8 -*-
# PROJECT_NAME : flapmmo
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
from .base import *

DEBUG = True

DATABASES = {

    'default': env.db_url(default='mysql://root:root@127.0.0.1:3306/flapmmo_dev'),
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}


STATICFILES_DIRS = (
    BASE_DIR + "/static-dev",
)

INSTALLED_APPS += ('django_extensions',)

MEDIA_URL = env('MEDIA_URL', default='/media/')

STATIC_URL = env('STATIC_URL', default='/static/')

# INSTALLED_APPS += ('debug_toolbar',)

INTERRNAL_IPS = env('INTERNAL_IPS', default='127.0.0.1')

INIT_SUPER_USER_NAME = env('SUPER_USERNAME', default='root')
INIT_SUPER_USER_PASS = env('SUPER_USERPASS', default='root')
INIT_SUPER_USER_EMAIL = env('SUPER_EMAIL', default='younger.x.shen@gmail.com')

# site name
SITE_NAME = env('SITE_NAME', default='flappmmo')

# wechat
WECHAT_KEY = env('WECHAT_KEY', default='')
WECHAT_SECRET = env('WECHAT_SECRET', default='')
GAME_SERVER = env('GAME_SERVER', default='test.game.com')


import time

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + "/log/" + time.strftime('%Y-%m-%d', time.localtime()) + '.log',
            'formatter': 'verbose'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'web': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        }
    }
}
