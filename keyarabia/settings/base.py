from pathlib import Path

import cloudinary
import dj_database_url
from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = SECRET_KEY = config("SECRET_KEY", default="django-insecure$simple.settings.local")

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "keyarabia.urls"

WSGI_APPLICATION = "keyarabia.wsgi.application"

# ==============================================================================
# INSTALLED APPS
# ==============================================================================

INSTALLED_APPS = [
   "django.contrib.admin",
   "django.contrib.auth",
   "django.contrib.contenttypes",
   "django.contrib.sessions",
   "django.contrib.messages",
   "django.contrib.staticfiles",
   "rest_framework",
   "rest_framework.authtoken",
   "dj_rest_auth",
   "drf_yasg",
   "cloudinary",
   "users",
   "employees",
]


SESSION_COOKIE_SECURE = False

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==============================================================================
# DATABASE SETTINGS
# ==============================================================================

DATABASES = {
    "legacy_db": dj_database_url.config(
        default=config(
            "DATABASE_URL",
            default="mysql://root:root1113@127.0.0.1:3306/riderkeys?init_command=SET sql_mode='STRICT_TRANS_TABLES'",
        ),
        conn_max_age=600,
    ),
    "default": dj_database_url.config(
        default=config(
            "DATABASE_URL",
            default="mysql://admin:yv2plm9mze3551dv@db-mysql-lon1-79982-do-user-3498265-0.b.db.ondigitalocean.com:25060/riderkeys",
        ),
        conn_max_age=600,
    ),
}

# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

##AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

AUTH_USER_MODEL = "users.Users"

REST_USE_JWT = True

JWT_AUTH_COOKIE = "access_token"

JWT_AUTH_REFRESH_COOKIE = "refresh_token"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
]

# ==============================================================================
# DJANGO REST FRAMEWORK SETTINGS
# ==============================================================================

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR.parent.parent / "static"

# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR.parent.parent / "media"

cloudinary.config(
    cloud_name=config("CLOUDINARY_NAME"),
    api_key=config("CLOUDINARY_API_KEY"),
    api_secret=config("CLOUDINARY_API_SECRET"),
    secure=True,
)

# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================

# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

APP_ENVIRONMENT = config("ENVIRONMENT", default="local")
