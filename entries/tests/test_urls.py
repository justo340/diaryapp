from django.test import TestCase
from django.urls import reverse, resolve
from entries.views import add, EntryListView


class TestUrls(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, EntryListView)

    def test_add_url_resolves(self):
        url = reverse('add')
        print(resolve(url))
        self.assertEqual(resolve(url).func, add)
