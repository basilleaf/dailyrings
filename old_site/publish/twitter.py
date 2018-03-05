# tweets as @dailyrings, runs on cron
from secrets import *

# Set up the Django Enviroment for running as shell script
from django.core.management import setup_environ 
import settings 
setup_environ(settings)

# script stuff
import tweepy
import urllib
from daily_image.views import *
import urllib2 

base_url = "http://dailyrings.org/"

# using is.gd
def shorten_url(long_url):
    try:
        base_url = 'http://is.gd/api.php?longurl=' + long_url
        tinyurl = urllib2.urlopen(base_url).read()
        return tinyurl
    except:
        print 'is.gd failed returning long url'
        return long_url    
    
try: 
    image = ImageForDate()
    url = base_url + str(image.pub_date)
    link = shorten_url(url) 
    tweet = str(image.tweet) + ' ' + link     

    # twitter auth stuff
    auth = tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET) 
    auth.set_access_token(TW_ACCESS_KEY, TW_ACCESS_SECRET)          
    api = tweepy.API(auth)  

    # tweet!    
    api.update_status(tweet)
    print 'tweeted http://twitter.com/dailyrings' + tweet

except:
    print 'failed to tweet:' 
