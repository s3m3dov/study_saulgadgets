# Stripe Payment Keys
STRIPE_API_KEY_PUBLISHABLE = "pk_test_51IWZgUHCGQv2kDWZiGaTNIsrKtEfoNQW23hLhCQ8RnmWBBr1rYFP3bkkv7oi9aJnxe73vW5gN2c5RY2V1XTGSwyX00PkarATdm"
STRIPE_API_KEY_HIDDEN = "sk_test_51IWZgUHCGQv2kDWZhswpEMdIG9DQp1Ltz75zE4zYlWCc3WdZCpz4c1BtI6pkYjk3h55P0oKdlIc0lybQpTzvcEGw00C3CWLjqZ"

# Razorpay Payment Keys
RAZORPAY_API_KEY_PUBLISHABLE = "rzp_test_z5vfzrbIZb9N3N"
RAZORPAY_API_KEY_HIDDEN = "0HtDa3tlEGdPze0EyHWtr1GD"

# * ----------------------------------------- * #
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Production Security Settings
ALLOWED_HOSTS = ['*']
SECRET_KEY = '(*0kk0bq8dgfj-10x*m1(g1szz4vo071+$_n_d68-9$6war=ar'
#! SECURITY WARNING: keep the secret key used in production secret!
DEBUG = True
#! SECURITY WARNING: don't run with debug turned on in production!

# Defined Authentication Settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'cart'
LOGOUT_REDIRECT_URL = 'frontpage'

# Email Server Settings
EMAIL_HOST = 'localhost' 
EMAIL_PORT = 1025

# Cart Sessions Settings
SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # sitemap
    'django.contrib.sitemaps',
    # My Apps
    'apps.core',
    'apps.store',
    'apps.cart',
    'apps.order',
    'apps.coupon',
    'apps.userprofile',
    'apps.newsletter',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'saulgadgets.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Our Context Processors
                'apps.store.context_processors.menu_categories',
                'apps.cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'saulgadgets.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'