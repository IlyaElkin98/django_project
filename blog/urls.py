from django.conf import settings
from django.urls import path


from .views import BlogCreateView, BlogListView, BlogDeleteView, BlogUpdateView, BlogDetailView
from django.conf.urls.static import static
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path("blogs/", BlogListView.as_view(), name="blogs"),
    path("blogs/new/", BlogCreateView.as_view(), name="create_blog"),
    path("blogs/delete_blog/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),
    path("blogs/detail_blog/<int:pk>/", BlogDetailView.as_view(), name="detail_blog"),
    path("blogs/detail_blog/<int:pk>/update/", BlogUpdateView.as_view(), name="update_blog")
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)