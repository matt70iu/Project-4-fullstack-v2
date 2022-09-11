from django.test import SimpleTestCase
from django.urls import reverse, resolve
from signup.views import UserCreateView


class TestUrls(SimpleTestCase):

    def test_register_url_resolved(self):
        url = reverse('create_user')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, UserCreateView)
