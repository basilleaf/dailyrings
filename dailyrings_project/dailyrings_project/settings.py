# Django settings for dailyrings project.
import os
Temp_Path = os.path.realpath('.')


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Lisa Ballard', 'lballard@seti.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': 'befoream_planetaryrings',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'befoream_ringweb',
        'PASSWORD': 'ringsnode42',
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "home/user/www/media/"
MEDIA_ROOT = '/home/befoream/www/media/rings/static_media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media.planetaryrings.com/static_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://media.planetaryrings.com/static_media/'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c1%r%_=%j$$^%=l_o&jgz4cpoz^o64&q$a-+6qzgdbs_bz^bsh'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'dailyrings_project.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/befoream/www/dailyrings/dailyrings_project/dailyrings/templates/',
    '/users/lballard/projects/dailyrings/gallery/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'dailyrings',
)

APP_START_DATE = '2010-09-26'
