from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Producer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detailview", args=[self.pk])


class Comment(models.Model):
    PRODUCT_STAR = {
        "1": "Very Bad",
        "2": "Bad",
        "3": "Good",
        "4": "Very Good",
        "5": "Perfect",
    }
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    star = models.CharField(max_length=10, choices=PRODUCT_STAR)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text