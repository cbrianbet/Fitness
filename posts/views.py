from django.shortcuts import render
from rest_framework import viewsets

from posts.apps import PostsConfig
from .models import Posts
from .serializers import PostSerializer


def blog(request):
    context = {
        'post': Posts.objects.all()
    }
    return render(request, 'posts/post.html', context)


class PostView(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
