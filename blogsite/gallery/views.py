from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import redirect , get_object_or_404
from .forms import ProductForm


def list_products(request):

    products = Product.objects.all()    
    context = {
        'products' : products
    }

    return render(request , 'gallery/index.html' ,context )

def product_detail(request ,pk):

    product = get_object_or_404(Product ,pk=pk)

    context = {'product':product}

    return render(request , 'gallery/detail.html' , context)

