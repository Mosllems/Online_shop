from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductListView(generic.ListView):
    # model = Product  # (agat be in sorat benevisim hameie mahsolat namayesh dade mishavand ama dar khat paein bar asas mojod bodan filter mishavand)
    queryset = Product.objects.filter(available=True)
    template_name = "products/product_list.html"
    context_object_name = "products"


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"
