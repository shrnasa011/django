from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import *
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    t=get_template('datetime.html')
    now=datetime.datetime.now()
    html=t.render(Context({'current_date':now}))
    
    return HttpResponse(html)

def datetimeplus(request, offset):

    try:
        off = int(offset)
    except ValueError:
        raise Http404()
  
    hour_offset=off
    
    next_time= datetime.datetime.now() + datetime.timedelta(hours=off)
   # assert False
    return render_to_response("hours_ahead.html", locals())
