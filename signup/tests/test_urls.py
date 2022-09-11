from django.test import SimpleTestCase
from django.urls import reverse, resolve
from signup.views import UserCreateView, UserEditView


class TestUrls(SimpleTestCase):

    def test_register_url_resolved(self):
        url = reverse('create_user')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, UserCreateView)

    def test_edit_profile_url_resolved(self):
        url = reverse('edit_profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, UserEditView)
