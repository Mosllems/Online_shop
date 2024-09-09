from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path("aboutus/", views.AboutUsView.as_view(), name="aboutus"),

    ]
