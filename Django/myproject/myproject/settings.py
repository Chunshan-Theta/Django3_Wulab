"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)

#from importlib import reload
import sys
sys.path.append(os.path.join(REPO_DIR, 'libs'))
#reload(sys)                         # 2
#sys.setdefaultencoding('utf-8')     # 3

import secrets
SECRETS = secrets.getter(os.path.join(DATA_DIR, 'secrets.json'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get('DEBUG') == 'True'
# if close DEBUG mode, Django would not process static file
# if you want to process static file without DEBUG mode, you should run 'manage.py runserver --insecure' 
DEBUG = 1
from socket import gethostname
ALLOWED_HOSTS = [
    '127.0.0.1',
    'theta-lab.tk',
    '140.115.126.216',# DON'T USE '*',if you site is for public.            
]

 






# Application definition
# please install rest_framework lib of Django first.
# install command: pip install djangorestframework

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'DemoProject',
    'RestAPI',
    'phd_status',
)
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
    )
'''
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.backends.signed_cookies',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
    )
'''
# GETTING-STARTED: change 'myproject' to your project name:
ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # GETTING-STARTED: change 'db.sqlite3' to your sqlite3 database:
        'NAME': os.path.join(DATA_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL =  '/Django_static/'


'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
'''
 
#session setting
SESSION_COOKIE_NAME = "sessionid"       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
SESSION_COOKIE_PATH = "/"               # Session的cookie保存的路径
SESSION_COOKIE_DOMAIN = None            # Session的cookie保存的域名
SESSION_COOKIE_SECURE = False       # 是否Https传输cookie
SESSION_COOKIE_HTTPONLY = True      # 是否Session的cookie只支持http传输
SESSION_COOKIE_AGE = 1209600        # Session的cookie失效日期（2周）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False # 是否关闭浏览器使得Session过期
SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存

# 加密cookie Session引擎
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies' 