from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path("contactus/", views.contact_us, name="contactus"),
    ]
