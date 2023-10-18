from django.urls import path, include
from .views import User

urlpatterns = [
    path("/login", User.login)
]
