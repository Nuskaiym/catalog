# -*- coding: utf-8 -*-
import os
import sys
virtual_env = os.path.expanduser('/home/host1732710/atehsys.kg/htdocs/virtualenv/')
activate_this = os.path.join(virtual_env,'bin/activate_this.py')
#execfile(activate_this, dict(__file__=activate_this))
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})
sys.path.append('/home/host1732710/atehsys.kg/htdocs/broadcast/')
sys.path.append('/home/host1732710/atehsys.kg/htdocs/broadcast/catalog/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'catalog.settings'
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
