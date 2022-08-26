from django.urls import path
from .views import UserCreateView, UserEdiView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='create_user'),
    path('edit_profile/', UserEdiView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(
        template_name='registration/change-password.html')),
    path(' password_success', views.password_success, name="password_success"),



]
