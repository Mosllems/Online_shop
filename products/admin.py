from django.contrib import admin
from .models import Product, Producer, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment
    fields = ["author", "text", "star", "active"]
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["title", "price", "producer", "available"]

    inlines = [CommentsInLine, ]


class ProducerAdmin(admin.ModelAdmin):
    model = Producer
    list_display = ["name", "phone_number", "address"]


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ["author", "product", "text", "star", "active"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Comment, CommentAdmin)