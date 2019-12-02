from .base import *


DEBUG = False

ALLOWED_HOSTS = secrets['ALLOWED_HOST']

DATABASES = {
    'default': secrets['DB_SETTINGS']['PRODUCTION']
}

CORS_ORIGIN_ALLOW_ALL = False  # 일단 TRUE -> 나중에 바꾸기
CORS_ORIGIN_ALLOW_WHITELIST = [
    'https://veeto-cli.gywls517.now.sh',
]