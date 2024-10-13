from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("User"))
    is_paid = models.BooleanField(default=False, verbose_name=_("Is paid?"))
    name = models.CharField(max_length=400, verbose_name=_("Name"))
    family_name = models.CharField(max_length=400, verbose_name=_("Family name"))
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone number"))
    address = models.CharField(max_length=700, verbose_name=_("Address"))
    order_note = models.TextField(blank=True, verbose_name=_("Order Note"))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    datetime_edited = models.DateTimeField(auto_now=True, verbose_name=_("Modified"))

    def __str__(self):
        return f"Order {self.id}"

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem {self.id} for product {self.product}"

    def get_total_price_each_item(self):
        return self.quantity * self.price
