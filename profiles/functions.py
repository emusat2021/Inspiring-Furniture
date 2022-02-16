""" This module contains different functions for the profile app """
from django.shortcuts import get_object_or_404
from .models import UserProfile
from products.models import Rating


def retrieve_purchased_products(request):
    """ Returns a dict with all purchased products """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    products_dict = {}
    for order in orders:
        for product_item in order.lineitems.all():
            # build a dictionary with unique product id
            # (for example, if user purchased same product on two different orders)
            if product_item.product.pk not in products_dict.keys():
                products_dict[product_item.product.pk] = product_item.product
    ratings = Rating.objects.all()

    # searching for a rating in all ratings
    # where the rating's product_id is equal to product's pk/id
    # and the rating's user_id is equal to current user's id.
    # if the rating is not found, then it is initialized with zero
    for item_k, item_v in products_dict.items():
        item_v.rating = 0
        item_v.review_text = ""
        item_v.rating_classes = []
        for rating in ratings:
            if rating.user_id_id == request.user.id and rating.product_id_id == item_v.pk:
                item_v.rating = rating.number_of_stars
                item_v.review_text = rating.review_text
                for x in range(int(item_v.rating)):
                    item_v.rating_classes.append("active")
                for x in range(5 - int(item_v.rating)):
                    item_v.rating_classes.append("inactive")
    return products_dict
