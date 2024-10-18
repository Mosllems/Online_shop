from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from orders.models import Order, OrderItem


class ProfileUpdate(generic.UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "username", "age", "email"]
    template_name = "profiles/myaccountupdate.html"
    success_url = reverse_lazy("userorder")

    def get_object(self):
        return self.request.user


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "profiles/myaccount.html", {"orders": orders})
