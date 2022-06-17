from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User' , on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField( auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)