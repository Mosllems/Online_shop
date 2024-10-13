from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.user_orders, name="userorder"),
    path('update/', views.ProfileUpdate.as_view(), name="profileupdate"),

    ]
