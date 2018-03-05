import os, sys
import django
import tweepy
import urllib, urllib2 
from time import sleep
from random import randint
from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

project_path = "/home/befoream/www/dailyrings/dailyrings_project/"
sys.path.append(project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyrings_project.settings")
django.setup()

# oh also 
sys.path.append('/home/befoream/www/dailyrings/dailyrings_project/')

from dailyrings.views import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyrings.settings")
django.setup()

from dailyrings.views import *

# script stuff
 
base_url = "http://dailyrings.org/"
base_path_images = '/home/befoream/www/media/rings/static_media/ring_images/'

image = ImageForDate()
url = base_url + str(image.pub_date)
tweet = str(image.tweet) + ' ' + url
tweet = ' '.join(tweet.split())  # removes carriage returns and double spaces

# twitter auth stuff
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# img path
img_path = base_path_images + image.jpg
fn = os.path.abspath(img_path)

# tweet!
api.update_with_media(fn, status=tweet)
print 'tweeted http://twitter.com/dailyrings' + tweet

# do followbacks
SCREEN_NAME = 'dailyrings'
# followers = api.followers_ids(SCREEN_NAME)
# friends = api.friends_ids(SCREEN_NAME)

followers = []
for block in tweepy.Cursor(api.followers_ids, SCREEN_NAME).items():
  followers += [block]

friends = []  # who we follow
for block in tweepy.Cursor(api.friends_ids, SCREEN_NAME).items():
    friends += [block]


to_follow = list(set(followers).difference(friends))

for f in to_follow:
    try:
        u = api.get_user(f)
        if not u.protected:  # don't try to follow private accounts
            sleep_time = randint(10,30)
            print "sleeping for %s" % sleep_time
            sleep(sleep_time)  # being a good twitizen 

            api.create_friendship(f)
            print('followed: ' + api.get_user(f).screen_name)

    except tweepy.error.TweepError, e:
          print(e.message[0]['message'])

# unfollow unfollowers
exceptions = ['Kaleidopix']
for f in friends:
    if f not in followers:
        if api.get_user(f).screen_name not in exceptions:
            sleep_time = randint(1,3)
            print "sleeping for %s" % sleep_time
            sleep(sleep_time)
            
            print "Unfollowing {0}".format(api.get_user(f).screen_name)
            api.destroy_friendship(f)
