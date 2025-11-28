from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("product/<int:pk>", views.product, name="product")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)