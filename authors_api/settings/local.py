from .base import *
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY", default="6mI-VSmpXQFIEIqBzsz_OpedXWmadWWMqgGSQgSd5A2HHQR9q3k")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
