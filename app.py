from django.conf.urls import patterns, url
from django.http import HttpResponse

## VIEWS ##

def index(request):
    return HttpResponse('Hello, world')

## ROUTES ##

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
)
