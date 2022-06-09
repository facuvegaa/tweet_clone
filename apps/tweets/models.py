from email.mime import image
from django.db import models
from django.forms import CharField

# Create your models here.

class Tweets(models.Model):
    content = models.TextField(max_length=250, blank=True, null=True) 
    image = models.FileField(upload_to='images/', blank=True, null=True)
