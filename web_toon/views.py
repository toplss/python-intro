from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Post
from .serializer import PostSerializer
import datetime as dt
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from bs4 import BeautifulSoup
import requests



# Create your views here.
@api_view(['GET'])
def home(request):
    posts = Post.objects.all()
    page = request.GET.get('page')
    
    paginator = Paginator(posts, 10)
    page_obj = paginator.page(page)

    serailized_posts= PostSerializer(page_obj, many=True)
    return Response(serailized_posts.data);
    
@api_view(['GET'])
def create_post(request):
    title = request.GET.get('title')
    author = request.GET.get('author')
    coverimg = request.GET.get('coverimg')
    created_at = dt.datetime.now()

    Post.objects.create(title=title, author=author, coverimg=coverimg, created_at=created_at)
    return Response('success');


@api_view(['GET'])
def crawl_data(request):
    url = 'https://www.naver.com/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

    return Response('ok');