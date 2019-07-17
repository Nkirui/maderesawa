from .base import*

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mconnection",
        "USER": "nathan",
        "PASSWORD": "monkey567",
        "HOST": "127.0.0.1",
        "PORT": '5432'
    }
}

if 'RDS_DB_NAME' in os.environ:

    DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mconnection",
        "USER": "nathan",
        "PASSWORD": "monkey567",
        "HOST": "127.0.0.1",
        "PORT":'5432'
     }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


