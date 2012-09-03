"""
shuffles the unpublished (and un-user-ordered) posts into random order by updating pub_order field
"""

# Set up the Django Enviroment for running as shell script
from django.core.management import setup_environ 
import settings 
setup_environ(settings)

from priod.daily_image.models import Image


# Nullify the pub_order for images that have not been manually ordered
# (this just makes it easier to see what is next, no duplicate numbers etc.
Image.objects.filter(user_ordered=False).update(pub_order=None)

# select images that have not been published yet or manually ordered in random order
# and set their pub_order to the random order
counter = 1
for image in Image.objects.filter(pub_date=None, user_ordered=False).order_by("?"):
    Image.objects.filter(pk=image.pk).update(pub_order=counter)
    counter+=1

