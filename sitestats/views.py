from django.shortcuts import render
from sitestats.models import SiteStats

def track_page_view(request):
    page = request.path
    try:
        stats = SiteStats.objects.get(page=page)
        stats.views += 1
        stats.save()
    except SiteStats.DoesNotExist:
        stats = SiteStats(page=page, views=1)
        stats.save()
    return render(request, 'base.html')
