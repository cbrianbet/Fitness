from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts
from .serializers import PostSerializer


def blog(request):
    return render(request, 'posts/post.html')


class PostView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
