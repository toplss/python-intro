from django.urls import path, include
from .views import home, create_post, crawl_data

urlpatterns = [
    path("/", home),
    path("/create", create_post),
    path("/crw", crawl_data),
]
