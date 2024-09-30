from django.db import models
from django.conf import Settings
from django.contrib.auth import get_user_model


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    name = models.CharField(max_length=400)
    family_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=700)
    order_note = models.TextField(blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem {self.id} for product {self.product}"
