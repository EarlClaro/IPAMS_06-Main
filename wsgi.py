# ipams_capstone2/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipams_capstone2.settings')

application = get_wsgi_application()