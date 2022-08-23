from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     context = {}
#     return render(request, 'home.html', context)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date', '-post_time']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    # fields = '__all__'


class NewCategoryView(CreateView):
    model = Category
    template_name = 'new_category.html'
    fields = '__all__'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
