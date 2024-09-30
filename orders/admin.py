from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    fields = ["order", "product", "quantity", "price"]
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ["user", "name", "family_name", "address", "datetime_created", "is_paid"]

    inlines = [OrderItemInLine, ]


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ["order", "product", "quantity", "price"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
