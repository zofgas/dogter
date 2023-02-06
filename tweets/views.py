

from django.shortcuts import render
from django.conf import settings


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    if request.user.is_aunthenticated:
        username = request.user.username
    return render(request, "pages/home.html", context={"username":username}, status=200)

def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html")


def tweets_detail_view(request,tweet_id, *args, **kwargs):
    return render(request, "tweets/detail.html", context={"tweet_id":tweet_id})


