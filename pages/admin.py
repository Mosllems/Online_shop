from django.contrib import admin

from .models import Message

class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ["user", "phone_number"]



admin.site.register(Message, MessageAdmin)