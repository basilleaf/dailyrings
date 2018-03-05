import sys
sys.path.append("/home/befoream/.local/lib/python2.6/site-packages/priod")


# Set up the Django Enviroment for running as shell script
from django.core.management import setup_environ 
import settings 
setup_environ(settings)

# script imports
from daily_image.views import *
sys.path.append('/home1/befoream/.local/lib/python2.6/site-packages/flickrapi-1.4.2-py2.5.egg')
import flickrapi

tags = 'space astronomy "planetary rings"'

# move me ####################
api_secret = '3edebd9e7cc61aad'
api_key = '49d7db3148406fc377dcc06ebe92afd5'
api_token = '72157625048598868-fd614dd036724d2c'
blog_id = '72157625048819580'
##############################

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
    filename = str(settings.MEDIA_ROOT + 'ring_images/' + jpg)
    flickr = flickrapi.FlickrAPI(api_key, api_secret, token=api_token, format='etree')
    result = flickr.upload(filename=filename, title=title, description = caption, tags = tags)
    print "posted " + name + ' - ' + title + ' to Flickr: http://www.flickr.com/photos/planetaryrings/'
except:
    print "FAIL posting to Flickr " + name + ' - ' + title 

