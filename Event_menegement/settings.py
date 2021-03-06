"""
Django settings for Event_menegement project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
# for gmail or googla apps
# -*- coding: utf-8 -*-

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pu+y0#w$ukel8v_%e3))p6hu7wcfyxol6(9sa_)nhus47*8gmb'

# SECURITY WARNING: don't run with debug turned on in production!
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
    'Account',
    'widget_tweaks',
    'slider',
    'social_django',
    'ckeditor',
    'create_event',
    'get_token',
    'events',
    'mydata',
]

AUTH_USER_MODEL='Account.UserProfile'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = [

    'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

LOGIN_REDIRECT_URL = 'index'
SOCIAL_AUTH_GITHUB_KEY = '1954766b696e62b69fa6'
SOCIAL_AUTH_GITHUB_SECRET = 'd268754188d58a3925a0bb312a580e997935e66e'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='499787962629-biutvj1ni5kp4bhgjhod835jui6rles2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='8TjxjlEifFWPEODDONNsHjE4'
# #
# SOCIAL_AUTH_FACEBOOK_KEY = '335746377029482'  # App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = 'a03c1d36d8a8d4d03b819b944b827a55'  # App Secret


ROOT_URLCONF = 'Event_menegement.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
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

WSGI_APPLICATION = 'Event_menegement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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



# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
LOGIN_REDIRECT_URL = 'index'

STATIC_URL = '/static/'
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

CKEDITOR_UPLOAD_PATH = "/media/"

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.mail.yahoo.com'
EMAIL_HOST_USER='saudbikash514@yahoo.com'#senders email address
EMAIL_HOST_PASSWORD='sauddevelopmentS514'
EMAIL_PORT=587
EMAIL_USE_TLS=False

#
# DEFAULT_FROM_EMAIL = 'noreply@khophi.co'
#
# SERVER_MAIL = 'noreply@khophi.co'


# Example for using Zoho Mail as email sending backend
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.zoho.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'noreply@khophi.co'
# EMAIL_HOST_PASSWORD = 'mypassword'
