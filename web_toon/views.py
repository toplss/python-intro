from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Post
from .serializer import PostSerializer
from django.core.paginator import Paginator
import datetime as dt


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