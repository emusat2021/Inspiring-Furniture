from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product


class TestOrderModel(TestCase):

    def setUp(self):
        Order.objects.create(
            order_number='test order number',
            full_name='test full name',
            email='test email',
            phone_number='test phonenumber',
            country='test country',
            postcode='test postcode',
            town_or_city='test town or city',
            street_address1="test street address 1",
            street_address2="test street address 1",
            date='test date',
            delivery_cost=2.93,
            order_total=108.54,
            grand_total=153.86,
            original_bag='test original bag',
            stripe_pid='test stripe pid'
        )

    def test_order_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_number').verbose_name
        self.assertEqual(field_label, 'order number')

    def test_order_number_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('order_number').max_length
        self.assertEqual(max_length, 32)

    def test_user_profile_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('user_profile').verbose_name
        self.assertEqual(field_label, 'user profile')

    def test_full_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('full_name').verbose_name
        self.assertEqual(field_label, 'full name')

    def test_full_name_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('full_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_email_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_phone_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')

    def test_phone_number_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 20)

    def test_country_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('country').verbose_name
        self.assertEqual(field_label, 'country')

    def test_country_number_blank_label(self):
        order = Order.objects.get(id=1)
        blank_label = order._meta.get_field('country').blank_label
        self.assertEqual(blank_label, 'Country *')
 
    def test_postcode_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('postcode').verbose_name
        self.assertEqual(field_label, 'postcode')

    def test_postcode_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('postcode').max_length
        self.assertEqual(max_length, 20)

    def test_town_or_city_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('town_or_city').verbose_name
        self.assertEqual(field_label, 'town or city')

    def test_town_or_city_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('town_or_city').max_length
        self.assertEqual(max_length, 40)

    def test_street_address1_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('street_address1').verbose_name
        self.assertEqual(field_label, 'street address1')

    def test_street_address1_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('street_address1').max_length
        self.assertEqual(max_length, 80)

    def test_street_address2_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('street_address2').verbose_name
        self.assertEqual(field_label, 'street address2')

    def test_street_address2_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('street_address2').max_length
        self.assertEqual(max_length, 80)
 
    def test_date_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_delivery_cost_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('delivery_cost').verbose_name
        self.assertEqual(field_label, 'delivery cost')

    def test_delivery_cost_max_digits_label(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('delivery_cost').max_digits
        self.assertEqual(max_digits, 6)

    def test_order_total_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('order_total').verbose_name
        self.assertEqual(field_label, 'order total')

    def test_order_total_max_digits_label(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('order_total').max_digits
        self.assertEqual(max_digits, 10)

    def test_grand_total_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('grand_total').verbose_name
        self.assertEqual(field_label, 'grand total')

    def test_grand_total_max_digits_label(self):
        order = Order.objects.get(id=1)
        max_digits = order._meta.get_field('grand_total').max_digits
        self.assertEqual(max_digits, 10)

    def test_original_bag_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('original_bag').verbose_name
        self.assertEqual(field_label, 'original bag')

    def test_stripe_pid_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('stripe_pid').verbose_name
        self.assertEqual(field_label, 'stripe pid')

    def test_stripe_pid_max_length_label(self):
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('stripe_pid').max_length
        self.assertEqual(max_length, 254)


class TestOrderLineItemModel(TestCase):

    def setUp(self):
        new_product = Product.objects.create(
            name='test product'
        )

        OrderLineItem.objects.create(
            product=new_product,
            lineitem_total=204.98
        )
