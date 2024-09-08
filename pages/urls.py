from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path("about us/", views.AboutUsView.as_view(), name="aboutus"),

    ]
