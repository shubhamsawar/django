from django.db import models
from django.conf import settings
import datetime

user = settings.AUTH_USER_MODEL

class news(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now())
    urls = models.URLField()
    img = models.URLField(null=True, blank=True)





    
    
    