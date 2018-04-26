from django.db import models
from django.db.models import Min
import datetime

class Archive(models.Model):
    # don't break the web
    name = models.CharField(max_length=30, primary_key=True)  # primary key
    pub_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = u'archives'

    
class ImageManager(models.Manager):
    def earliest(self):
        """ returns earliest pub_date as datetime.datetime"""
        earliest_pub = Archive.objects.aggregate(Min('pub_date'))['pub_date__min']
        earliest_pub = datetime.datetime.fromordinal(earliest_pub.toordinal())
        return earliest_pub
    
class Image(models.Model):
    name = models.CharField(max_length=30, primary_key=True)  # primary key
    title = models.CharField(max_length=200)
    tweet = models.CharField(max_length=140)
    caption = models.TextField()
    credit = models.CharField(max_length=250)
    more_info = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    planet = models.CharField(max_length=7)
    jpg = models.CharField(max_length=200)
    pub_date = models.DateField(null=True, blank=True)
    pub_order = models.IntegerField(null=True, blank=True)
    user_ordered = models.BooleanField(default=False)
    image_fail = models.BooleanField(default=False)
    
    pub_dates = ImageManager()
    objects = models.Manager()


    class Meta:
        db_table = u'images'
        ordering = ('pub_order',)

    def __unicode__(self):  
        return u'%s %s' % (self.name, self.title)        

                                                           
    def save(self, *args, **kwargs):
        model = self.__class__

        if self.pub_order is None:
            # Append
            try:
                last = model.objects.order_by('-pub_order')[0]
                self.pub_order = last.pub_order + 1
            except IndexError:
                # First row
                self.pub_order = 0

        return super(Image, self).save(*args, **kwargs)
