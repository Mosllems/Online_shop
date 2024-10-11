from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from accounts.models import CustomUser


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class AboutUsView(generic.TemplateView):
    template_name = "pages/aboutus.html"


class MyAccount(generic.TemplateView):
    model = CustomUser
    template_name ="pages/myaccount.html"
    context_object_name = "accounts"


class ProfileUpdate(generic.UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "username", "age", "email"]
    template_name = "pages/myaccountupdate.html"
    success_url = reverse_lazy("myaccount")

    def get_object(self):
        return self.request.user
