import os
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UNBABEL_API_USERNAME = 'fullstack-challenge'
UNBABEL_API_KEY = '9db71b322d43a6ac0f681784ebdcc6409bb83359'
UNBABEL_URL = 'https://sandbox.unbabel.com/tapi/v2/translation/'

HEADERS = {
    "Authorization": "ApiKey {0}:{1}".format(
                                        UNBABEL_API_USERNAME,
                                        UNBABEL_API_KEY
                                    ),
    "Content-Type": "application/json"
}

SERVER_NAME = 'localhost:8000'
#SERVER_NAME = '0.0.0.0:8000'

SECRET_KEY = '89798a7df987asd987y&T&*7886as8dfya9sd8fy98790&(*SD&S*(DS&*DYS*'

SQLALCHEMY_DATABASE_URI = 'postgresql://unbabel:unbabel@postgres:5432/unbabel'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
PROPAGATE_EXCEPTIONS = True

CELERY_BROKER_URL = 'redis://:unbabel@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:unbabel@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'unbabel.get_translateds',
        'schedule': timedelta(seconds=30)
    },
}

DEBUG_TB_INTERCEPT_REDIRECTS = False