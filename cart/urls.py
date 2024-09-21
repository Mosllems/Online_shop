from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.cart_detail_view, name="cart_detail"),
    path("add/<int:product_id>/", views.add_to_cart_view, name="cart_add"),
    path("remove/<int:product_id>/", views.delete_from_cart, name="cart_remove"),
    path("clear/", views.clear_form, name="cart_clear"),

]
