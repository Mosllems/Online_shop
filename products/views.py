from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm


class ProductListView(generic.ListView):
    # model = Product.objects.all()  # (agar be in sorat benevisim hameie mahsolat namayesh dade mishavand ama dar khat paein bar asas mojod bodan filter mishavand)
    paginate_by = 4
    queryset = Product.objects.filter(available=True).order_by("-price")
    template_name = "products/product_list.html"
    context_object_name = "products"

    # def get_queryset(self):
    #     queryset = Product.objects.filter(available=True)
    #     return queryset

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_comment = product.comments.filter(active=True)

    if request.method == "POST":
        comment = CommentForm(request.POST)  # az roie form CommentForm ke request an post ast yek object misazim
        if comment.is_valid():
            comment = comment.save(commit=False)  # comment ra zakhire mikonim commit=false yani nariz to database va felan negahdar va an ra mirizim dar yek motaqaier
            comment.product = product
            comment.author = request.user
            comment.save()
            messages.success(request, _("Your comment has been added successfully"))
            comment = CommentForm()
    else:
        comment = CommentForm()

    return render(request, "products/product_detail.html", {
        "product": product,
        "comments": product_comment,
        "comment_form": comment,
        "product_form": AddToCartProductForm,
    })

def search_view(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        products = Product.objects.filter(title__icontains=searched)
        return render(request, "products/searched_product.html", {"searched": searched, "products": products})
    if request.method == "GET":
        return render(request, "products/searched_product.html")