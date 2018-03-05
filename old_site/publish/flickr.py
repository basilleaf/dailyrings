# flickr posts as  http://www.flickr.com/photos/planetaryrings 
# runs on cron
from secrets import *

# Set up the Django Enviroment for running as shell script
from django.core.management import setup_environ 
from secrets import *
import settings 
setup_environ(settings)

# script imports
from daily_image.views import *
import flickrapi

tags = 'space astronomy "planetary rings"'

# get today's image
image = ImageForDate()
name = str(image.name)
title = str(image.title)
caption = str(image.caption)
credit = str(image.credit)
jpg = image.jpg
image_url = image.image_url
pub_date = image.pub_date
caption = caption + "<p>credit: " + credit + "</p>"

# post to flickr
try: 
    filename = str(settings.MEDIA_ROOT + jpg)
    flickr = flickrapi.FlickrAPI(flickr_api_key, flickr_api_secret, token=flickr_api_token, format='etree')
    result = flickr.upload(filename=filename, title=title, description = caption, tags = tags)
    print "posted " + name + ' - ' + title + ' to Flickr: http://www.flickr.com/photos/planetaryrings/'
except:
    print "FAIL posting to Flickr " + name + ' - ' + title 

