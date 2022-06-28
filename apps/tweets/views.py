import random
from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from twitter_clone_backend.settings import ALLOWED_HOSTS


from .models import Tweets
from .forms import TweetForm
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello</h>")
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    print(is_ajax(request))
    form =  TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None

    if form.is_valid():

        obj = form.save(commit=False)
        obj.save()
        if is_ajax(request):
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and url_has_allowed_host_and_scheme(url=next_url, allowed_hosts=ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm() 
    if form.errors:
        if is_ajax(request):
            return JsonResponse(form.errors, status=400)
    return render(request, "components/form.html", context={"form" : form})



def tweet_list_view(request, *args, **kwargs):
    qs = Tweets.objects.all()
    tweet_list = [x.serialize() for x in qs]
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

