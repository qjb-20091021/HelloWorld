

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e8kmibbzz*a!6_(z@it#nk6lb=e@p!ppmo)&!*9p7lwdugm4#p'

# SECURITY WARNING: don't run with debug turned on in production!
class TrueFalse(object):
    pass


DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notice',
    'mod',
    'park',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HelloWorld.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]


WSGI_APPLICATION = 'HelloWorld.wsgi.application'



DATABASES = \
{
    'default':
    {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'bsznpark',		#数据库的名字
        'USER': 'sa',		#登录数据库的用户名
        'PASSWORD': 'sa123-',	#登录数据库的密码
        'HOST': 'localhost',	#数据库的IP地址
        'PORT': '1433',		#数据库的端口
        'OPTIONS':
        {
              'driver':'SQL Server Native Client 10.0',	#注意，不行就试试11.0
              'MARS_Connection': True,
         },
    }
}

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



LANGUAGE_CODE = 'zh-hans'

TIME_ZONE =  'Asia/Shanghai'  # 指定时间

USE_I18N = True

USE_L10N = True

#USE_TZ = True



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'notice/static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("imges", os.path.join(STATIC_ROOT, 'imges')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("html", os.path.join(STATIC_ROOT, 'html')),
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
]

