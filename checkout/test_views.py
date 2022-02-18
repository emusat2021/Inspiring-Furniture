from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import cache_checkout_data, checkout, checkout_success


class TestProfilesViews(SimpleTestCase):

    def test_view_cache_checkout_data_resolves(self):
        url = reverse('cache_checkout_data')
        self.assertEqual(resolve(url).func, cache_checkout_data)

    def test_view_checkout_resolves(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_view_checkout_success_resolves(self):
        url = reverse('checkout_success', args=['order_number'])
        self.assertEqual(resolve(url).func, checkout_success)
