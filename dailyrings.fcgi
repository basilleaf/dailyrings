#!/home1/befoream/python27/bin/python27
import sys, os
project_name = "dailyrings_project"
app_name = 'dailyrings'
 
# Add a custom Python path.
sys.path.insert(0, os.path.expanduser("~") + "/python27")
sys.path.insert(13, os.getcwd() + "/" + project_name)
 
os.environ['DJANGO_SETTINGS_MODULE'] = project_name + '.settings'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
