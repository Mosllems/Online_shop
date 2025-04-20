from django.conf import settings
from django.db import models


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=800, default="<NAME>")
    email = models.EmailField(default='<EMAIL>')
    phone_number = models.CharField(max_length=15)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


