"""
gets media associated with recently imported data (via parser.py or manual entry)
the filter on the first image.objects getter query 
tells it to only get that which has not had an order assigned to it
only entries from parser.py that haven't gone thru shuffle.py will be in that state
so you can get only media for new imports
"""
local_base_dir = '/users/lballard/projects/priod/new_images/'

# Set up the Django Enviroment for running as shell script
from django.core.management import setup_environ 
import settings 
setup_environ(settings)

from priod.daily_image.models import Image
import os.path, urllib

errors = []
for image in Image.objects.filter(pub_order__isnull=True):
    url   = image.image_url + image.jpg
    fname = local_base_dir  + image.jpg
    if not os.path.isfile(fname):
        try:
            urllib.urlretrieve( url, fname )
            Image.objects.filter(pk=image.pk).update(image_fail=False)
            print "got:  " + image.jpg
        except:
            Image.objects.filter(pk=image.pk).update(image_fail=True)
            print "fail: " + image.jpg
            errors += ['fail: ' + url]
            
print "Finished!"
for e in errors:
    print e


