from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
import random

from .models import Tweets
# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello</h>")
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    qs = Tweets.objects.all()
    tweet_list = [{"id" : x.id, "content" : x.content, "likes" : random.randint(0, 1234)} for x in qs]
    data = {
        "response":  tweet_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id):
    data = {
    "id" : tweet_id,   
    } 
    status = 200
    try:
        obj = Tweets.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not found"
        status = 404

    return JsonResponse(data, status=status)