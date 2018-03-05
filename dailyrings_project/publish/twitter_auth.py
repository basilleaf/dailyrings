import tweepy
CONSUMER_KEY = 'gnX2q45LkHpYNrToaB1Q'
CONSUMER_SECRET = 'CB8O6m2gAoNpQsHyI9d70jybhf5wvzs43nHZUCrA'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)
print "ACCESS_KEY = '%s'" % auth.access_token.key
print "ACCESS_SECRET = '%s'" % auth.access_token.secret

