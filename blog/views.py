from django.shortcuts import render
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


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', ]
    success_url = reverse_lazy('blog:blogs')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blogs')