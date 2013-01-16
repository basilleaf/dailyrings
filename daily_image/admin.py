from django.contrib import admin
from django import forms
from django.db import models
from priod.daily_image.models import Image
import settings
             
# a custom Textarea widget             
class DifferentlySizedTextarea(forms.Textarea):
  def __init__(self, *args, **kwargs):
    attrs = kwargs.setdefault('attrs', {})
    attrs.setdefault('cols', 40)
    attrs.setdefault('rows', 3)
    super(DifferentlySizedTextarea, self).__init__(*args, **kwargs)
  
# Image admin  
class ImageAdmin(admin.ModelAdmin):
    list_display = ('name','planet','thumbnail','title','tweet','pub_date','pub_order')
    list_editable = ('tweet','pub_order')       
    search_fields = ('name', 'title')
    list_filter = ('pub_date',)
    ordering = ('pub_order',)       

    # use custom widget for CharField fields
    formfield_overrides = { models.CharField: {'widget': DifferentlySizedTextarea}}
    
    # where to find the thumbnail to show in the list
    def thumbnail(self, instance): 
        if settings.DEBUG == True: # being janky here
            return '<img src="/static_media/%s" width="100"/>' % instance.jpg 
        return '<img src="' + settings.ADMIN_MEDIA_PREFIX + '%s" width="200"/>' % instance.jpg 
        
    thumbnail.allow_tags=True 

admin.site.register(Image, ImageAdmin)


