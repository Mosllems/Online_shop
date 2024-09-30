from django.urls import path, include
from . import views


urlpatterns = [
    path("create/", views.order_create, name="order_create"),

]
