from django.shortcuts import render
from sitestats.models import SiteStats
from django.db.models import F

# Create your views here.

def index(request):
    # Get all SiteStats objects that match the current URL
    site_stats = SiteStats.objects.filter(url=request.path_info)

    if site_stats.exists():
        # If there is an existing SiteStats object, update its views count
        site_stats.update(views=F('views') + 1)
    else:
        # If there is no existing SiteStats object, create a new one with views=1
        SiteStats.objects.create(url=request.path_info, views=1)

    return render(request, 'home/index.html')


