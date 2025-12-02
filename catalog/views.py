from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class CatalogListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    template_name = "contacts.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = 'product'

