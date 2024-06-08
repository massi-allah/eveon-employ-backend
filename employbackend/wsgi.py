import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()
settings_module = os.getenv('DJANGO_SETTINGS_MODULE', 'employbackend.settings.production')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
