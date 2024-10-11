from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('profile/', views.MyAccount.as_view(), name="myaccount"),
    path('update/', views.ProfileUpdate.as_view(), name="profileupdate"),
    path("aboutus/", views.AboutUsView.as_view(), name="aboutus"),

    ]
