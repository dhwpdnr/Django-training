from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY", default="6mI-VSmpXQFIEIqBzsz_OpedXWmadWWMqgGSQgSd5A2HHQR9q3k")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@apiimmperfect.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"
