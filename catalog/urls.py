from django.conf import settings
from django.urls import path
from .views import CatalogListView, ProductDetailView, ContactsView
from django.conf.urls.static import static
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", CatalogListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>", ProductDetailView.as_view(), name="product")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)