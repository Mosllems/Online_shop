from django.shortcuts import render
from django.views import generic


def order_create(request):
    return render(request, "orders/order_create.html")