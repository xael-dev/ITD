"""
WSGI config for WebsiteITD project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/applicationusr/ITD/ITDenv/'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebsiteITD.settings')

application = get_wsgi_application()
