from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8#k*hf=p7qooohh-d7meni&91kzsl8rd1*4*9+%v(2e#uxzo=&'

DEBUG = True

ALLOWED_HOSTS = ["*"]  # 🔥 allow local + deploy later


# ===================== APPLICATIONS =====================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'rest_framework',
    'channels',
    'django_crontab',

    # your apps
    'users',
    'network',
    'trips',
    'carpool',
    'payments',
]


# ===================== MIDDLEWARE =====================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # ⚠️ keep CSRF for now (safe)
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


# ===================== URLS =====================

ROOT_URLCONF = 'core.urls'


# ===================== TEMPLATES =====================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]


# ===================== ASGI / WSGI =====================

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'


# ===================== DATABASE =====================

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===================== AUTH =====================

AUTH_USER_MODEL = 'users.User'


# ===================== PASSWORD VALIDATION =====================

AUTH_PASSWORD_VALIDATORS = [

    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},

]


# ===================== INTERNATIONAL =====================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True


# ===================== STATIC =====================

STATIC_URL = 'static/'

# ⚠️ FIX: avoid warning
STATICFILES_DIRS = [
    BASE_DIR / "static"
] if (BASE_DIR / "static").exists() else []


# ===================== CHANNELS =====================

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}


# ===================== REST FRAMEWORK =====================

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny"
    ]
}


# ===================== CRON JOBS =====================

CRONJOBS = [
    ('*/1 * * * *', 'trips.tasks.simulate_trips'),
]