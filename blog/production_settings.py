import dj_database_url, os
from .settings import * # 含入原本的settings.py所有設定
# heroku使用的資料庫為PostgreSQL，所以要修改資料庫設定



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': 'db',
        'POST': '5432',
    }
}

STATIC_ROOT = 'staticfiles'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') # 設定HTTP連線方式
ALLOWED_HOSTS = ['*'] # 讓所有的網域都能瀏覽本網站
DEBUG = False