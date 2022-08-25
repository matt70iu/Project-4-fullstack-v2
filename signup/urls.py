from django.urls import path
from .views import UserCreateView, UserEdiView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='create_user'),
    path('edit_profile/', UserEdiView.as_view(), name='edit_profile'),



]
