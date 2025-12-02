from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from blog.models import Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image', ]
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blogs')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(publication_sign__gt=0)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object



class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', ]

    def get_success_url(self):
        return reverse('blog:detail_blog', kwargs={'pk' : self.object.pk})

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blogs')