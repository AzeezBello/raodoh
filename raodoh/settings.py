"""
Django settings for raodoh project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import cloudinary
from decouple import config, Csv


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_DIR = os.path.join(BASE_DIR, 'static')

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'crispy_forms',
    'social_django',
    'django_countries',
    'corsheaders',
    'pwa',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'raodoh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'raodoh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = (
    # 'social.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    # 'social_core.backends.google.GoogleOpenId',  # for Google authentication
    # 'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'django.contrib.auth.backends.ModelBackend',
)


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # '/var/www/static/',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Django Crispyform settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'


LOGIN_URL = config('LOGIN_URL')
LOGOUT_URL = config('LOGOUT_URL')
LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL')


# SOCIAL_AUTH_URL_NAMESPACE = config('SOCIAL_AUTH_URL_NAMESPACE')
# SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')  # App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')  # App Secret
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')  # App ID
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')  # App Secret
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL')
# SOCIAL_AUTH_LOGIN_URL = '/oauth/'


# # Production environment settings
# SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', cast=bool)
# SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int)
# SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', cast=bool)
# SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', cast=bool)
# SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', cast=bool)
# SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool)
# SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', cast=bool)
# CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', cast=bool)
# X_FRAME_OPTIONS = config('X_FRAME_OPTIONS')


# EMAIL_BACKEND During development only
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# EMAIL_BACKEND production config (Gmail)
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# EMAIL_BACKEND = config('EMAIL_BACKEND')


# OTHER EMAIL SETTINGS #
########################
# ADMIN_EMAIL = config('ADMIN_EMAIL')
# SUPPORT_EMAIL = config('SUPPORT_EMAIL')
# DEFAULT_FROM_EMAIL = ADMIN_EMAIL
# SERVER_EMAIL = ADMIN_EMAIL


# Cloudinary config

# cloudinary.config(
#     cloud_name=config('CLOUDINARY_CLOUD_NAME'),
#     api_key=config('CLOUDINARY_API_KEY'),
#     api_secret=config('CLOUDINARY_API_SECRET')
# )


# django-cors config
# https://pypi.org/project/django-cors-headers/

# CORS_ORIGIN_ALLOW_ALL = config('CORS_ORIGIN_ALLOW_ALL', cast=bool)

# CORS_ALLOW_CREDENTIALS = config('CORS_ALLOW_CREDENTIALS', cast=bool)

# CORS_ALLOW_METHODS =config('CORS_ALLOW_METHODS', cast=Csv())

# CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST', cast=Csv())

# CORS_ORIGIN_REGEX_WHITELIST = config('CORS_ORIGIN_REGEX_WHITELIST', cast=Csv())


# Keep our policy as strict as possible
# CSP_DEFAULT_SRC = ("'none'",)
# CSP_STYLE_SRC = ("'self'", 'stackpath.bootstrapcdn.com')
# CSP_SCRIPT_SRC = ("'self'", 'code.jquery.com')
# CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com', 'fonts.googleapis.com')
# CSP_IMG_SRC = ("'self'",'res.cloudinary.com')


# django-progressive-web-app config
# PWA_APP_NAME = 'Radodoh'
# PWA_APP_DESCRIPTION = ""
# PWA_APP_THEME_COLOR = '#0A0302'
# PWA_APP_BACKGROUND_COLOR = '#ffffff'
# PWA_APP_DISPLAY = 'standalone'
# PWA_APP_SCOPE = '/'
# PWA_APP_ORIENTATION = 'any'
# PWA_APP_START_URL = '/'
# PWA_APP_ICONS = [{'src': '/static/img/', 'sizes': '160x160'}]
# PWA_APP_SPLASH_SCREEN = [{'src': '/static/img/ScholarX.png', 'media': '(device-width: 320px) and (device-height: '
#                                                                       '568px) and (-webkit-device-pixel-ratio: 2)'}]
# PWA_APP_DIR = 'ltr'
# PWA_APP_LANG = 'en-US'
#
#
# # logging config
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'mysite.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#         'MYAPP': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#         },
#     }
# }