from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.cart_detail_view, name="cart_detail")

]
