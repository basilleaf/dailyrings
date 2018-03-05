from django.contrib.syndication.views import Feed
from django.utils import feedgenerator
from dailyrings.models import Image
import datetime
import time

class GMT5(datetime.tzinfo): 
    def utcoffset(self,dt):  #51/2 hours ahead of GMT 
        return datetime.timedelta(hours=5,minutes=30) 
    
    def tzname(self,dt): 
        return "GMT +5" 
    
    def dst(self,dt): 
        return datetime.timedelta(0)      


class LatestImagesFeed(Feed):
    title = "Planetary Ring Image of the Day"
    link = "/"
    description = "Sharing one unique image of planetary rings each day. Stunning NASA photos of the rings of Saturn, Jupiter, Neptune, and Uranus."
    def items(self):
        return Image.objects.filter(pub_date__range=["1999-09-23", datetime.datetime.today() ]).order_by('-pub_date')[:15]

    def item_title(self, item):
        return item.title
        
    def item_description(self, item):
        desc = '<img width = "600" src = "' + 'http://media.planetaryrings.com/static_media/ring_images/' + str(item.jpg) + '"> '
        desc += item.caption
        return desc
        
    def item_link(self,item):
        return 'http://dailyrings.org/' + str(item.pub_date)
    
    def item_pubdate(self,item):                                                
        return datetime.datetime(*(time.strptime(str(item.pub_date) + ' 08:00','%Y-%m-%d %H:%M')[0:6]))







