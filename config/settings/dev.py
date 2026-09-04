from .base import *

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-4&!1!f186a^_a!f%gv*00j1w9i@b#sd-0%$ej*z)!1a19rusg-"
)

DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
