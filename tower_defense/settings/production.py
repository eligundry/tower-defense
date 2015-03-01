from .base import *

DEBUG = False
# WSGI_APPLICATION = 'ws4redis.django_runserver.application'

try:
	from .local import *
except ImportError:
	pass
