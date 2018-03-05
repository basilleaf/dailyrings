from daily_image.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404     
from django.core.paginator import Paginator, EmptyPage
                                  

def gallery(request, **kwargs): 
                             
    template= kwargs['template'] + '.html'
    
    image_per_page = 100                                                                    
 
    page = 1 if 'page' not in kwargs else kwargs['page']

    today = datetime.datetime.today()
    earliest = Image.pub_dates.earliest() 
      
    
    try:                         
        images = Image.objects.exclude(pub_date=None).order_by('-pub_order').values()
        for i in images:                                                              
            i['str_date'] = str(i['pub_date'])
            
        images = Paginator(images, image_per_page).page(page).object_list 
                       
    except EmptyPage:
        raise Http404
        
    return render_to_response(template,locals(), context_instance=RequestContext(request)) 
       
   
def preview(request, **kwargs):
    img = get_object_or_404(Image, pub_date=kwargs['date'] )
    return render_to_response('preview.html',locals(), context_instance=RequestContext(request)) 
    
    
    
            
    
    
    
    