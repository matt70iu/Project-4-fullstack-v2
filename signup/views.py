''' Required imports
'''
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from mainblog.models import Profile
from .forms import RegistrationForm, EditProfileForm, PasswordChangedForm,\
    ProfilePageForm


def my_login(request):
    '''Checks username/password is valid when logging in
    '''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully")
            return redirect('home')
        else:
            messages.success(request, "Invalid details, please try again")
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {})


def my_logout(request):
    '''Logs user out with success message
    '''
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('home')


class CreateProfilePageView(CreateView):
    ''' Renders user profile creation tamplate
    and saves user profile data with success message.
    '''
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.INFO,
                             'Profile created successfully')
        return super().form_valid(form)


class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    ''' Renders user edit profile template
    and saves data with success message
    '''
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_picture', 'website_url',
              'facebook_url', 'instagram_url', 'twitter_url']
    success_url = reverse_lazy('home')
    success_message = "Your profile has been edited successfully!"


class MainProfilePageView(DetailView):
    '''Renders user profile info'''

    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(MainProfilePageView, self).get_context_data(
            *args,  **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    '''Renders password change form, confirms with success message'''

    form_class = PasswordChangedForm
    success_url = reverse_lazy('home')
    success_message = "Your password has been changed successfully!"


class UserCreateView(SuccessMessageMixin, generic.CreateView):
    '''Renders user registration form, confirms with success message'''

    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account has been successfully registered please \
     login."


class UserEditView(SuccessMessageMixin, generic.UpdateView):
    '''Renders user profile edit form, confirms with success message'''

    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    success_message = "Your account info has been succesfully edited"

    def get_object(self):
        return self.request.user
