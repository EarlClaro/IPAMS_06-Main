import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('SECRET_KEY', '6Ld-guEbAAAAANAgbmQI2Ph6knhKsOglaOEEuyp3')

DEBUG = os.environ.get("DEBUG", "False").lower() == 'true'

ALLOWED_HOSTS = ['26.34.129.27', '127.0.0.1', 'localhost', '192.168.203.205', 'windows-nginx', '*']

AUTH_USER_MODEL = 'accounts.User'

LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

INSTALLED_APPS = [
    'accounts',
    'file_management',
    'records',
    'notifications',
    "crispy_forms",
    'crispy_bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django_extensions',
    'axes',
    "sslserver",
    "debug_toolbar",
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    'django_auto_logout.middleware.auto_logout',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ipams.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'ipams/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_auto_logout.context_processors.auto_logout_client',
                'notifications.context_processors.notificationCount',
                'records.context_processors.subscription_status'
            ],
        },
    },
]

WSGI_APPLICATION = 'ipams.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', 'ipamsdjango'),
        'USER': os.environ.get('DB_USER', 'root'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'new_password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
    'nalc': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('NALC_DB_NAME', 'nalc_schema'),
        'USER': os.environ.get('NALC_DB_USER', 'root'),
        'PASSWORD': os.environ.get('NALC_DB_PASSWORD', 'new_password'),
        'HOST': os.environ.get('NALC_DB_HOST', 'localhost'),
        'PORT': os.environ.get('NALC_DB_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'
USE_I18N = True
USE_L10N = False
USE_TZ = False

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True

AUTO_LOGOUT = {
    'IDLE_TIME': 1800,
    'MESSAGE': 'You have been idle for too long. Please login again to continue.',
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
}

AXES_FAILURE_LIMIT = 3
AXES_ENABLE_ADMIN = True
AXES_ONLY_USER_FAILURES = True
AXES_LOCKOUT_URL = '/lockout'
AXES_RESET_ON_SUCCESS = True

GOOGLE_RECAPTCHA_SECRET_KEY = '6Lckj-EbAAAAAEKoK1quZBP62i5NY57NlqDko-kL'
GOOGLE_RECAPTCHA_SITE_KEY = '6Lckj-EbAAAAAHKCPuWWZCsDMD48xYL8XYc0OPOt'
TEST_FORM = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ipamsdevteam2024@gmail.com'
EMAIL_HOST_PASSWORD = 'ufub nxrb odrd ismt'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

CSRF_TRUSTED_ORIGINS = ['https://*.ap.ngrok.io/']
INTERNAL_IPS = ['localhost', 'ipams']

MIGRATION_MODULES = {
    'accounts': 'accounts.disable_migrations',
    'records': 'records.disable_migrations',
    'notifications': 'notifications.disable_migrations',
}

X_FRAME_OPTIONS = 'SAMEORIGIN'

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
