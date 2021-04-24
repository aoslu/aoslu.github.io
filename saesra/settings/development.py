from .base import *

DEBUG=True

ALLOWED_HOSTS = []

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DEV ORTAMINA ÖZEL DB.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
