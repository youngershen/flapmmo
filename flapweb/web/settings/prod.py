# -*- coding:utf-8 -*-
# PROJECT_NAME : flapmmo
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com
import time
from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

CACHES = {

    'default': env.cache_url()
}

# site name
SITE_NAME = env('SITE_NAME')

COMPRESS_OFFLINE = True

DATABASES = {

    'default': env.db_url()
}


MEDIA_URL = env('MEDIA_URL')

STATIC_URL = env('STATIC_URL')

INIT_SUPER_USER_NAME = env('SUPER_USERNAME')
INIT_SUPER_USER_PASS = env('SUPER_USERPASS')
INIT_SUPER_USER_EMAIL = env('SUPER_EMAIL')

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
            'level': 'ERROR',
        },
        'web': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        }
    }
}

WECHAT_KEY = env('WECHAT_KEY')
WECHAT_SECRET = env('WECHAT_SECRET')
GAME_SERVER = env('GAME_SERVER')