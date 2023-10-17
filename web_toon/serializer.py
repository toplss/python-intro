from django.core import serializers
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'coverimg', 'created_at', 'updated_at']
        id      = serializers.CharField(max_length=True)
        title   = serializers.CharField(max_length=100)
        author  = serializers.CharField(max_length=20)
        coverimg = serializers.FileField(max_length=100)
        created_at = serializers.DateTimeField(input_formats=["%Y-%m-%d"])
        updated_at = serializers.DateTimeField(input_formats=["%Y-%m-%d"])
