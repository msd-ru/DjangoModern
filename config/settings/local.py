from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default = 'django-insecure-+&$axgzg)r3d%zzzuvf32=6=#a8p(q8&0)99m7ysa-!6^x$0n=')

DEBUG = env.bool('DJANGO_DEBUG', default=True)