from django.contrib.contenttypes.models import ContentType
from .models import PageView

def log_page_view(request, obj):
    content_type = ContentType.objects.get_for_model(obj.__class__)
    object_id = obj.id
    try:
        page_view = PageView.objects.get(content_type=content_type, object_id=object_id)
    except PageView.DoesNotExist:
        page_view = PageView(content_type=content_type, object_id=object_id)
    page_view.view_count += 1
    page_view.save()
