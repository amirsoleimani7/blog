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


def edit_project(request , pk):

    product = get_object_or_404(Product , pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index_page')
    else:
        form = ProductForm(instance=product)
        return render(request)
        