import os, sys
activate_this = '/home/{Ваш логин}/domains/{Ваш логин}.xsph.ru/django-example/venv/bin/activate_this.py'
with open(activate_this) as f:
   exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/{Ваш логин}/domains/{Ваш логин}.xsph.ru/django-example/'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_example.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
