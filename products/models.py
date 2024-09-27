from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class Producer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(default="lorem ipsum", blank=False)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Product Image", upload_to="covers/", blank=True)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detailview", args=[self.pk])


class Comment(models.Model):
    PRODUCT_STAR = {
        "1": _("Very Bad"),
        "2": _("Bad"),
        "3": _("Good"),
        "4": _("Very Good"),
        "5": _("Perfect"),
    }
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(verbose_name=_("Comment Text"))
    star = models.CharField(max_length=10, choices=PRODUCT_STAR, verbose_name=_("What is your score?"))
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-datetime_created"]
