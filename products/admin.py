from django.contrib import admin
from .models import Product, Producer


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("title", "price", "producer", "available")


class ProducerAdmin(admin.ModelAdmin):
    model = Producer
    list_display = ("name", "phone_number", "address")


admin.site.register(Product, ProductAdmin)
admin.site.register(Producer, ProducerAdmin)
