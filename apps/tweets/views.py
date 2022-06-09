from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Tweets
# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello</h>")

def tweet_detail_view(request, tweet_id):
    try:
        obj = Tweets.objects.get(id=tweet_id)
    except:
        raise Http404
    
    data = {
        "id" : obj.id,
        "content" : obj.content, 
        #"image_path": obj.image  
        }
    return HttpResponse(f"<h1>ID: {obj.id} CONTENT: {obj.content}</h>")