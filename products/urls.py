from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="listview"),
    path("<int:pk>/", views.product_detail_view, name="detailview"),
    path("search", views.search_view, name="search"),

]
