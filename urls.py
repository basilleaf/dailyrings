from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from daily_image.views import *
from daily_image.feeds import LatestImagesFeed

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^feed/$', LatestImagesFeed() ),
)

urlpatterns += patterns('daily_image.views',
    (r'^$', today),
    (r'^(\d{4}-\d{2}-\d{2})/$', dailyImage),
    (r'^search/', search),
)    

if settings.DEBUG:                         
    urlpatterns += patterns('django.views.static',
    (r'^static_media/(?P<path>.*)$',
        'serve', {
        'document_root': '/Users/lballard/projects/priod/static_media/',
        'show_indexes': True }),)

