
# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personalPortfolio.settings')

# application = get_wsgi_application()
# app = application

# personalPortfolio/wsgi.py

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personalPortfolio.settings')

# Get the Django application
django_application = get_wsgi_application()

# Wrap the Django application with WhiteNoise
application = WhiteNoise(django_application)

# Add the static and media file serving configurations
application.add_files(os.path.join(os.path.dirname(__file__), 'staticfiles'), prefix='/static/')
application.add_files(os.path.join(os.path.dirname(__file__), 'media'), prefix='/media/')

