from pathlib import Path
import os
import redis
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

GOOGLE_OAUTH_CLIENT_ID = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "corsheaders",
    "accounts",
    "todos",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

# CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOW_HEADERS = default_headers + (
#     "accept",
#     "accept-encoding",
#     "authorization",
#     "content-type",
#     "dnt",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
# )

# CORS_ALLOW_METHODS = [
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# ]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "HOST": os.getenv("DATABASE_HOST"),
#         "PORT": os.getenv("DATABASE_PORT"),
#         "NAME": os.getenv("DATABASE_NAME"),
#         "USER": os.getenv("DATABASE_USER"),
#         "PASSWORD": os.getenv("DATABASE_PASSWORD"),
#     }
# }

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_CONNECTION_POOL = redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    max_connections=300,
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[%(asctime)s] <%(process)s> [%(levelname)s] %(message)s",
            "datefmt": "%d/%b/%Y:%H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "console": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        }
    },
}


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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = False

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "sign_in"
LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "sign_in"

LAB_TOKEN = os.getenv("LAB_TOKEN")

NOTEBOOK_ARGUMENTS = [
    "--ip=0.0.0.0",
    "--port=8888",
    "--no-browser",
    "--allow-root",
    f"--LabApp.token='{LAB_TOKEN}'",
    "--LabApp.base_url='/notebooks'",
    "--ServerApp.allow_remote_access=true",
]
