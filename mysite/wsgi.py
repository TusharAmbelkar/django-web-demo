"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import threading
import os

import visiondemo.external_app as startup
t = threading.Thread(target=startup.run)
t.start()

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)


