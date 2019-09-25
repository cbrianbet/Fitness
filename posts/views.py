from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts
from .serializers import PostSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
