from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm


class ProductListView(generic.ListView):
    # model = Product  # (agat be in sorat benevisim hameie mahsolat namayesh dade mishavand ama dar khat paein bar asas mojod bodan filter mishavand)
    queryset = Product.objects.filter(available=True).order_by("-price")
    template_name = "products/product_list.html"
    context_object_name = "products"


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_comment = product.comments.all()

    if request.method == "POST":
        comment = CommentForm(request.POST)  # az roie form CommentForm ke request an post ast yek object misazim
        if comment.is_valid():
            comment = comment.save(commit=False)  # comment ra zakhire mikonim commit=false yani nariz to database va felan negahdar va an ra mirizim dar yek motaqaier
            comment.product = product
            comment.author = request.user
            comment.save()
            comment = CommentForm()
    else:
        comment = CommentForm()

    return render(request, "products/product_detail.html", {
        "product": product,
        "comment": product_comment,
        "comment_form": comment,
        "product_form": AddToCartProductForm,
    })
