from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostView)

urlpatterns = [
    path('rest/', include(router.urls)),
    path('post/', views.blog, name='post')
]