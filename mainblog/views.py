''' Required imports'''
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView,\
    DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
# pylint: disable=no-member


def LikeView(request, pk):
    ''' Asigns/removes like from post'''
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    '''renders home page posts vew'''
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date', '-post_time']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    '''renders posts filtered by catagory on homepage'''

    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html',
                  {'cats': cats.title(), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    '''Renders main post page'''
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        items = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = items.total_likes()

        liked = False
        if items.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class NewPostView(SuccessMessageMixin, CreateView):
    '''Renders create post page'''
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    success_url = reverse_lazy('home')
    success_message = "New post has been created!"


class NewCommentView(CreateView):
    '''Renders new comment page'''
    model = Comment
    form_class = CommentForm
    template_name = 'new_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        messages.add_message(self.request, messages.INFO,
                             'Comment added successfully')
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class NewCategoryView(SuccessMessageMixin, CreateView):
    '''Renders template to add catagory'''
    model = Category
    template_name = 'new_category.html'
    success_url = reverse_lazy('home')
    success_message = "New Catagory has been created!"
    fields = '__all__'


class EditPostView(SuccessMessageMixin, UpdateView):
    '''Renders edit post view template'''
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    success_message = "Post has been successfully updated!"


class DeletePostView(DeleteView):
    '''Renders delete post view'''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = 'your post has been successfully deleted!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)
