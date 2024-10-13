from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from accounts.models import CustomUser
from orders.models import Order, OrderItem


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class AboutUsView(generic.TemplateView):
    template_name = "pages/aboutus.html"

