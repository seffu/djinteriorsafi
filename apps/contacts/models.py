from django.db import models
from datetime import datetime


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=200, blank=True)
    subject = models.CharField(max_length=200, blank=False)
    message = models.TextField(blank=False)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name