from django.urls import path
from .views import UserCreateView, UserEdiView, PasswordsChangeView, MainProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='create_user'),
    path('edit_profile/', UserEdiView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
    path(' password_success', views.password_success, name="password_success"),
    path('<int:pk>/profile/', MainProfilePageView.as_view(),
         name='show_profile_page'),
    path('<int:pk>/profile_page/', EditProfilePageView.as_view(),
         name='edit_profile_page'),
    path('create_user_profile_page/', CreateProfilePageView.as_view(),
         name='create_profile_page'),




]
