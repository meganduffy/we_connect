from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config(
    "mysql://be7e855bf7d62c:66cc4b48@eu-cdbr-west-01.cleardb.com/heroku_f373066c6c1d6bc")
#
# DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
#
# DATABASES['default']['NAME'] = os.path.join(BASE_DIR, 'db.sqlite3')
#
# CLEAR_DB_URL = os.environ.get("CLEARDB_DATABASE_URL", "")
#
# DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)

ALLOWED_HOSTS = ['we-connect.herokuapp.com']

# Paypal environment variables
SITE_URL = 'https://we-connect.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://we-connect.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'meganemilyduffy@gmail.com'