from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationForm, EditProfileForm, PasswordChangedForm, ProfilePageForm
from mainblog.models import Profile
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.INFO,
                             'Profile created successfully')
        return super().form_valid(form)


class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_picture', 'website_url',
              'facebook_url', 'instagram_url', 'twitter_url']
    success_url = reverse_lazy('home')
    success_message = "Your profile has been edited successfully!"


class MainProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainProfilePageView, self).get_context_data(
            *args,  **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangedForm
    success_url = reverse_lazy('home')
    success_message = "Your password has been changed successfully!"


class UserCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account has been successfully registered, please login."


class UserEdiView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    success_message = "Your account info has been succesfully edited"

    def get_object(self):
        return self.request.user
