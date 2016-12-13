from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
import datetime

# Create your views here.
def home(request):
    return HttpResponse("This will be the home page eventually")

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, hour_offset):
    try:
        hour_offset = int(hour_offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    return render(request, 'hours_ahead.html', {'next_time':next_time})