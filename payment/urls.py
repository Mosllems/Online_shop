from django.urls import path, include
from . import views

urlpatterns = [
    path("process/", views.process_payment, name="process_payment"),

]

