from django.shortcuts import render
from django.views.generic import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from web_toon.models import Post

# Create your views here.
class User(View):

    @api_view(['POST'])
    def login(request):
        user_id = request.data.get('user_id')
        password = request.data.get('password')
        print(user_id)
        return Response('test')
