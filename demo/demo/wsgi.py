import os
import sys
import site

os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'

SITE_ROOT = os.path.dirname(os.path.dirname( __file__ ))
site.addsitedir( SITE_ROOT + '/venv/local/lib/python2.7/site-packages' )

sys.path.append( SITE_ROOT )

activate_env=os.path.expanduser(SITE_ROOT + "/venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
