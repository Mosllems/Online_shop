from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart


@login_required
def order_create(request):
    order_from = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, "Your cart is empty please purchase something")
        return redirect("listview")

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item["product_obj"]
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item["quantity"],
                    price=product.price,
                )
            cart.clear()
            messages.success(request, "Your Order has successfully placed")

    return render(request, "orders/order_create.html", context={
        "form": order_from,
    })
