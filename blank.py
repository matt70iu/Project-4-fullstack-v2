<div class="col-md-8 offset-md-2">
    {% for message in messages %}
    <div class="alert {{ message.tags }} alert-dismissible fade show" id="msg" role="alert">
        {{ message | safe }}

    </div>
    {% endfor %}


    from django.views.generic.edit import DeleteView
    from django.core.urlresolvers import reverse_lazy
    from django.contrib import messages
    from .models import Thing

    class ThingDelete(DeleteView):
    model = Thing
    success_url = reverse_lazy('list')
    success_message = "Thing was deleted successfully."

    def delete(self, request, *args, **kwargs):
    messages.success(self.request, self.success_message)
    return super(ThingDelete, self).delete(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
    response = super().delete(request, *args, **kwargs)
    messages.success(self.request, 'Your post has been deleted sucessfully!')
    return response




    class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
    user = form.get_user()
    messages.success(self.request, f'Welcome {user}')
    return super().form_valid(form)