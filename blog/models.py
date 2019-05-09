from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

