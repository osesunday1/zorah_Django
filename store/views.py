from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from category.models import Category
from packages.models import Packages
from surprises.models import Surprises
# Create your views here.




def store (request, category_slug=None, packages_slug=None, surprises_slug=None):
    packages = None
    categories = None
    surprises = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    
    elif packages_slug != None:
        packages = get_object_or_404(Packages, slug=packages_slug)
        products = Product.objects.filter(packages=packages, is_available=True)
        product_count = products.count()

    elif surprises_slug != None:
        surprises = get_object_or_404(Surprises, slug=surprises_slug)
        products = Product.objects.filter(surprises=surprises, is_available=True)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True).order_by('created_date')
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }

    return render (request, 'store/store.html', context)



def all_products (request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    context = {
        'products': products,
    }
    return render (request, 'store/all-products.html', context)



def productdetail(request, pk):
    product= Product.objects.get(id=pk)
    

    context = {'product': product,}
    return render(request, 'store/product-detail.html',context)
