from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart


@login_required
def order_create(request):
    order_from = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _("Your cart is empty please purchase something"))
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
            messages.success(request, _("Your Order has successfully placed"))
            send_mail(subject=_('Your Order has been registered'),
                      message=_('Your Order has been registered successfully thanks for your purchase'),
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[request.user.email],
                      fail_silently=False
                      )


    return render(request, "orders/order_create.html", context={
        "form": order_from,
    })
