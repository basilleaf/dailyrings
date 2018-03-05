from django.conf.urls import url, patterns, include
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from dailyrings.views import today, dailyImage, search
from dailyrings.feeds import LatestImagesFeed

urlpatterns = [   
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed/$', LatestImagesFeed() ),
]

urlpatterns = [
    url(r'^$', today),
    url(r'^(\d{4}-\d{2}-\d{2})/$', dailyImage),
    url(r'^search/', search),
]

"""
if settings.DEBUG:                         
    urlpatterns += patterns('django.views.static',
    url(r'^static_media/(?P<path>.*)$',
        'serve', {
        'document_root': '/Users/lballard/projects/dailyrings/static_media/',
        'show_indexes': True }),)
"""
