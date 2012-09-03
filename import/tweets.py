# writes tweets and saves to db for each record

# Set up the Django Enviroment for running as shell script
import sys
sys.path.append('~/projects/')
sys.path.append('~/priod/')
from priod import settings  
from django.core.management import setup_environ 
setup_environ(settings)

from stripogram import html2text, html2safehtml
from priod.daily_image.models import Image
from HTMLParser import HTMLParser
from urlparse import urlparse
import exceptions, urllib2, re

images = Image.objects.all();
for image in images:
    tweet_text = ''.join(html2safehtml(image.caption.split('.')[0], valid_tags=()).split("\n")).strip()
    tweet_text = tweet_text.strip(',')
    
    url_len = len('http://is.gd/ggapu');
    # the tweet text can be 140 minus the url and title length 
    # and spaces after each 
    tweet_length = 140 + len(image.title.strip()) + 2 + len(tweet_text) + 1 + url_len; 

    tweet = image.title.strip() + ': ' + tweet_text.strip()
    if (len(tweet) > 140):
        # this tweet will be to long so need to trim it.
        
        # this is how long the tweet can be: 
        max_length = 140-3-url_len # since we are trimming make room for 2 ellipses: .. 

        while (tweet_length > max_length):
            tweet_arr = tweet.split(' ')
            tweet_arr.pop()
            tweet = ' '.join(tweet_arr) # pop off the last word
            tweet_length = len(tweet)

        tweet = tweet + '..'
        
        if ((len(tweet) + 1 + url_len) > 140):
            print 'length will exceed 140 by ' + str(len(tweet)) + "\n" + tweet
            raise Exception("fail")
        
    image.tweet = tweet
    image.save()
    print "saved: " + tweet + "\n\n"    

print "\n\n Bye! \n\n"