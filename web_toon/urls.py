from django.urls import path, include
from .views import home, create_post

urlpatterns = [
    path("/", home),
    path("/create", create_post)
]
