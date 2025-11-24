from django.urls import path
from . import views
from catalog.views import home, contacts, one_product

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("one_product/<int:pk>", views.one_product, name="one_product")
]