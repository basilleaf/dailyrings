"""
this script parses the pds-rings press release gallery tree at 
base_url = "http://pds-rings.seti.org/saturn/cassini/"

if an image already exists in the database it is updated

to get only the most recent month set latest_month_only to True
"""
latest_month_only = True # like I was really going to do this monthly

# Set up the Django Enviroment for running as shell script
from django.core.management import setup_environ 
import settings 
setup_environ(settings)

# script imports
from stripogram import html2text, html2safehtml
from priod.daily_image.models import Image
from HTMLParser import HTMLParser
from urlparse import urlparse
import exceptions, urllib2, re

base_url = "http://pds-rings.seti.org/saturn/cassini/"

# set to strict imports, ie want to know if an url is too long for field
from django.db import connection
cursor = connection.cursor()
cursor.execute("SET SQL_MODE = 'STRICT_ALL_TABLES'")

# get all the monthly gallery pages
print "scanning " + base_url
homepage     = urllib2.urlopen(base_url).read()
list_pages   = re.findall("HREF=\"([0-9]+-[0-9]+)\.html", homepage)

# get all the detail pages
detail_pages = []
for page_name in list_pages:
    print "scanning gallery page " + page_name
    list_page = urllib2.urlopen(base_url + page_name + ".html").read()
    detail_pages += re.findall("HREF=\"\./(.*)\.html", list_page) 
    if latest_month_only: break
    
    
# scrape each detail page
errors = []
for page_name in detail_pages:
    url = base_url + page_name + '.html'
    
    try:
        print "opening " + url
        page = urllib2.urlopen(url).read()
    except HTTPError:   
        print "failed at " + url
        errors += [url] 
    
    print "scraping " + url
    try:
        name,title = re.search("<title>(.*)</title>", page).group(1).split(':')
        name       = name.strip()
        title      = title.strip()

        more_info = "http://pds-rings.seti.org/saturn/cassini/" + name

        caption    = re.search("Original Caption Released with Image:(.*)Image Credit:", page, re.DOTALL | re.UNICODE).group(1).strip()
        caption    = html2safehtml(caption,valid_tags=("p","a","img","br")).strip()

        credit     = re.search("Image Credit:(.*)<br>", page, re.DOTALL | re.UNICODE).group(1).strip()
        credit     = html2safehtml(credit,valid_tags=("p","a","img")).strip()

        # find images
        image_url = re.search("href\t*=\t*\"(.*)\.tif\"", page).group(1)
        image_url = urlparse(image_url).netloc

        if not image_url: image_url = base_url
        else:  image_url = 'http://' + image_url + '/'

        jpg       = 'jpeg/'    + name.strip() + '.jpg'
        jpg_mod   = 'jpegMod/' + name.strip() + '_modest.jpg'
        tif       = 'tiff/'    + name.strip() + '.tif'

    except:
        errors += ["could not parse " + url]
        print "failed " + url
        continue
    
    
    try: 
        pub_date=Image.objects.get(pk=name).pub_date
        user_ordered=Image.objects.get(pk=name).user_ordered
        pub_order=Image.objects.get(pk=name).pub_order
    except Image.DoesNotExist: 
        pub_date = None
        user_ordered = False 
        pub_order = None
            
    # update db
    image = Image(name=name,title=title,caption=caption,more_info=more_info,credit=credit,image_url=image_url,jpg=jpg,pub_date=pub_date,user_ordered=user_ordered,pub_order=pub_order)
    try:
        image.save()
        print name + " saved \n"
    except:        
        print "failed " + url
        errors += ["could not save to db" + url]

print "finished! "
print ""
if len(errors): print "HTTP Errors could not load the following pages\n"
for e in errors:
    print e + "\n"

