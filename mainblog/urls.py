from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, NewPostView, EditPostView, DeletePostView, NewCategoryView, CategoryView, LikeView, NewCommentView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('new_post/', NewPostView.as_view(), name='new_post'),
    path('new_category/', NewCategoryView.as_view(), name='new_category'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment', NewCommentView.as_view(), name='new_comment'),


]
