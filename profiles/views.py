from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import UserProfile
from .forms import UserProfileForm
from . import functions
from checkout.models import Order
from products.models import Rating, Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history_list(request):
    """ Display all user's orders. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/order_history_list.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display one user's order. """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def review_list(request):
    """ Display a list of unique purchased products for the current user. """
    products_dict = functions.retrieve_purchased_products(request)
    template = 'profiles/review_list.html'
    context = {
        'products': products_dict,
    }

    return render(request, template, context)


@login_required
def delete_rating(request, product_id):
    """ Delete a rating or a review_text, given the product_id and 'type' argument """
    if 'type' not in request.GET:
        return redirect(reverse('review_list'))
    type = request.GET["type"]

    products_dict = functions.retrieve_purchased_products(request)
    if product_id not in products_dict:
        messages.warning(request, 'You are not allowed to delete the rating for this product until you purchased it!')
        return redirect(reverse('review_list'))

    rating = get_object_or_404(Rating, product_id_id=product_id, user_id_id=request.user.id)
    if type == "rating":
        rating.number_of_stars = 0
        rating.save()
        messages.success(request, 'Rating deleted!')
    if type == "review_text":
        rating.review_text = ""
        rating.save()
        messages.success(request, 'Review message deleted!')
    return redirect(reverse('review_list'))


@login_required
def edit_rating(request, product_id):
    """ Edit a rating or a review_text, given the product_id and 'type' argument """
    if 'type' not in request.GET:
        return redirect(reverse('review_list'))
    type = request.GET["type"]
    number_of_stars = 0
    review_text = ""
    if 'number_of_stars' in request.GET:
        number_of_stars = request.GET["number_of_stars"]
    if 'review_text' in request.GET:
        review_text = request.GET["review_text"]

    products_dict = functions.retrieve_purchased_products(request)
    if product_id not in products_dict:
        messages.warning(request, 'You are not allowed to rate this product until you purchased it!')
        return redirect(reverse('review_list'))

    # https://stackoverflow.com/questions/14255125/catching-doesnotexist-exception-in-a-custom-manager-in-django
    # try to find a record in the database for the current respective product_id and current user
    # if there is no record in the database then we need to create it in the except block
    # we create the record first, otherwise get_object_or_404 would generate an error
    try:
        rating = Rating.objects.get(product_id_id=product_id, user_id_id=request.user.id)
    except ObjectDoesNotExist:
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#saving-objects
        # build a Rating object with the product_id, user_id, number_of_stars and review_text
        rating = Rating(product_id=Product(product_id), user_id=User(request.user.id), number_of_stars=number_of_stars, review_text=review_text)
        # save the object in the database
        rating.save()

    rating = get_object_or_404(Rating, product_id_id=product_id, user_id_id=request.user.id)
    if type == "rating":
        rating.number_of_stars = number_of_stars
        rating.save()
        messages.success(request, 'Rating updated!')
    if type == "review_text":
        rating.review_text = ""
        rating.save()
        messages.success(request, 'Review message deleted!')
    return redirect(reverse('review_list'))
