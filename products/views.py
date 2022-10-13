from django.shortcuts import render
from django.views.generic import DetailView
from products.models import Product
import products



class ProductDetailView (DetailView):
    queryset = Product.objects.all()
    print(queryset)
    template_name = "products/detailed.html"
    def Products(DetailView):
        items = Product.objects.all()
    context = {
        'items': items
    }