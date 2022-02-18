from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestBagViews(SimpleTestCase):

    def test_view_bag_resolves(self):
        url = reverse('view_bag')
        self.assertEqual(resolve(url).func, view_bag)

    def test_add_to_bag_resolves(self):
        url = reverse('add_to_bag', args=['item_id'])
        self.assertEqual(resolve(url).func, add_to_bag)

    def test_adjust_bag_resolves(self):
        url = reverse('adjust_bag', args=['item_id'])
        self.assertEqual(resolve(url). func, adjust_bag)

    def test_remove_from_bag_resolves(self):
        url = reverse('remove_from_bag', args=['item_id'])
        self.assertEqual(resolve(url).func, remove_from_bag)
