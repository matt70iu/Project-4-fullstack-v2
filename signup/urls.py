from django.urls import path
from .views import UserCreateView, UserEditView, PasswordsChangeView, MainProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='create_user'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
    path('<int:pk>/profile/', MainProfilePageView.as_view(),
         name='show_profile_page'),
    path('<int:pk>/profile_page/', EditProfilePageView.as_view(),
         name='edit_profile_page'),
    path('create_user_profile_page/', CreateProfilePageView.as_view(),
         name='create_profile_page'),
    path('my_login', views.my_login, name="login"),
    path('my_logout', views.my_logout, name="logout"),





]
