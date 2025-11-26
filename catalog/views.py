from django.shortcuts import render

from catalog.models import Product

def home(request):
    products_list = Product.objects.all()
    context = {'products_list' : products_list, }
    return render(request, "home.html", context)

def contacts(request):
    return render(request, "contacts.html")

def product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product, }
    return render(request, "product.html", context)
