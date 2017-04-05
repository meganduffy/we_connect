from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse(
    "mysql://b7df457a0b883e:4cc7bd23@eu-cdbr-west-01.cleardb.com/heroku_f73334689795fd1")

ALLOWED_HOSTS.append(['we-connect.herokuapp.com', 'fb2eea7a.ngrok.io'])

# Paypal environment variables
SITE_URL = 'https://we-connect.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://we-connect.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'meganemilyduffy@gmail.com'