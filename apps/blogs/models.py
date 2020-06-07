from django.db import models
from datetime import datetime


# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    blog_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    blog_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
