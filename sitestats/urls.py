from django.urls import path
from .views import track_page_view

urlpatterns = [
    path('<path:path>/', track_page_view),
]
