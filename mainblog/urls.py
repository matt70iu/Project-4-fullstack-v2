from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, NewPostView, EditPostView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('new_post/', NewPostView.as_view(), name='new_post'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='update_post'),


]
