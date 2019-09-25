from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=200)
    date = models.DateTimeField()

