import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=*i_@=9vr1@8ndqh#6r0-q)v%zw@o+^qmgp0=odcbxi^=ao5z!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG')
ALLOWED_HOSTS = [os.environ.get('DJANGO_DOMAIN_NAME')]
CSRF_COOKIE_DOMAIN = os.environ.get('DJANGO_DOMAIN_NAME')
SESSION_COOKIE_AGE = 60 * 60 * 24
SESSION_ENGINE = 'django.contrib.sessions.backends.db'


# Application definition
INSTALLED_APPS = (
    #'modeltranslation',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    #'django.contrib.sites',
    'django_user_agents',
    'haystack',
    'tinymce',
    'admin_honeypot',
    'compressor',
    'filebrowser',
    'logentry_admin',
    'session_security',
    'auditlog',
    'admin_reorder',
    'hitcount',
    'simple_history',
    'sitemap',
    'django_extensions',
    'django_rq',
    'autosave',
)
RQ_QUEUES = {
    'default': {
        'HOST': 'redis',
        'PORT': 6379,
        'DB': 2,
    }
}
#SITE_ID=1
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    }
}
HITCOUNT_KEEP_HIT_ACTIVE = {'days': 1}
HITCOUNT_HITS_PER_IP_LIMIT = 0
HITCOUNT_KEEP_HIT_IN_DATABASE = {'days': 1}

HTML_MINIFY = False
ADMIN_REORDER = (
        # Rename app
        {'app': 'admin_honeypot', 'label': 'Ловушка'},
        {'app': 'defender', 'label': 'Авторизации'},
        {'app': 'auth', 'label': 'Пользователи'},
        {'app': 'logentry_admin', 'label': 'История'},
        )
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware'
)

ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, os.environ.get('DJANGO_TEMPLATES'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.core.context_processors.static',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'OPTIONS': {
            'connect_timeout': 10,
        }
    },
}
LANGUAGE_CODE = os.environ.get('DJANGO_LANGUAGE_CODE')
DATE_FORMAT = os.environ.get('DJANGO_DATE_FORMAT')
DATETIME_FORMAT = os.environ.get('DJANGO_DATETIME_FORMAT')
USE_I18N = True
USE_L10N = True
TIME_ZONE = os.environ.get('DJANGO_TIMEZONE')
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
COMPRESS_ENABLED = True
COMPRESS_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "staticfiles"),
#)
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
MEDIA_URL = '/media/'

NEWS_PER_PAGE = 10
ARTICLES_PER_PAGE = 10

TINYMCE_DEFAULT_CONFIG = {
    'height': 500,
    'plugins': 'paste',
    'paste_as_text': 'true',
    'selector': 'textarea',
    'forced_root_block': 'p',
    'file_browser_callback': 'mce_filebrowser',
    'theme': 'advanced',
}

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = ''

IS_DEFENDER_ENABLED = True
if IS_DEFENDER_ENABLED:
    DEFENDER_LOGIN_FAILURE_LIMIT = 5
    DEFENDER_COOLOFF_TIME = 90000
    DEFENDER_REDIS_URL = 'redis://redis:6379/'+os.environ.get('DJANGO_REDIS_NUM')
    INSTALLED_APPS += ('defender',)
    MIDDLEWARE_CLASSES += ('defender.middleware.FailedLoginMiddleware',)


SESSION_EXPIRE_AT_BROWSER_CLOSE = True
GRAPPELLI_ADMIN_TITLE = os.environ.get('DJANGO_ADMIN_TITLE')

#RECAPTCHA_PRIVATE_KEY = ""

LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(asctime)s %(pathname)s -> %(funcName)s %(message)s'
                },
            },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.dirname(os.path.abspath(__file__))+'/../logs/'+os.environ.get('DJANGO_LOGFILE'),
                'formatter': 'simple',
                },
             'console': {
                 'class': 'logging.StreamHandler',
                 'stream': sys.stdout,
                 'formatter': 'simple',
                 },
            },
        'loggers': {
            'default': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propogate': True,
                },
            },
        }

TIME_ZONE ='Europe/Moscow'

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        #'pympler',
    )
    MIDDLEWARE_CLASSES += (
    )
    STATIC_URL = '/static/'
    #STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    CSRF_COOKIE_DOMAIN = os.environ.get('DJANGO_DOMAIN_NAME')
    SESSION_SECURITY_INSECURE = True

    DEBUG_TOOLBAR_PANELS = [
                'debug_toolbar.panels.versions.VersionsPanel',
                'debug_toolbar.panels.timer.TimerPanel',
                'debug_toolbar.panels.settings.SettingsPanel',
                'debug_toolbar.panels.headers.HeadersPanel',
                'debug_toolbar.panels.request.RequestPanel',
                'debug_toolbar.panels.sql.SQLPanel',
                'debug_toolbar.panels.staticfiles.StaticFilesPanel',
                'debug_toolbar.panels.templates.TemplatesPanel',
                'debug_toolbar.panels.cache.CachePanel',
                'debug_toolbar.panels.signals.SignalsPanel',
                'debug_toolbar.panels.logging.LoggingPanel',
                'debug_toolbar.panels.redirects.RedirectsPanel',
                'debug_toolbar.panels.timer.TimerDebugPanel',
                #'pympler.panels.MemoryPanel',
             ]
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    COMPRESS_ENABLED = False
