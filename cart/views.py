from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .cart import Cart
from .forms import AddToProductForm
from products.models import Product


def cart_detail_view(request):
    return render(request, "cart/cart_detail.html", )


def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = AddToProductForm(request.POST)
    if form is vars():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data["quantity"]
        cart.add(product, quantity)
    return redirect("cart_detail")


