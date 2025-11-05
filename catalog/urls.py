from django.urls import path
from . import views
from catalog.views import home, contacts

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts")
]