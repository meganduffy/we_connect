from base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['we-connect.herokuapp.com']

# Paypal environment variables
SITE_URL = 'https://we-connect.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://we-connect.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'meganemilyduffy@gmail.com'