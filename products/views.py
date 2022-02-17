from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Rating
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # calculate average rating for the products
    # convert all ratings into a list
    ratings_obj = Rating.objects.all()
    ratings = []
    for rating in ratings_obj:
        ratings.append(rating)

    # adjust rating property to the average of ratings for each product
    # average_rating: avergage rating
    # rating_classes: average_rating rounded to the nearest integer used for css classes
    products_with_ratings = []
    for product in products:
        product.average_rating = "N/A"
        product.rating_classes = []
        # find all ratings for the current product
        product_ratings = [x.number_of_stars for x in ratings if x.product_id_id == product.pk]
        # if ratings were found, then calculate average_rating for the current product
        if len(product_ratings) != 0:
            # convert decimal to 1 digit after point: https://stackoverflow.com/a/455634
            product.average_rating = "{:.1f}".format(sum(product_ratings) / len(product_ratings))
            for item in range(round(float(product.average_rating))):
                product.rating_classes.append("active")
            for item in range(5 - round(float(product.average_rating))):
                product.rating_classes.append("inactive")

        products_with_ratings.append(product)

    context = {
        'products': products_with_ratings,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    product.rating_classes = []
    ratings = Rating.objects.all()
    # find all ratings for the current product
    product_ratings = [x.number_of_stars for x in ratings if x.product_id_id == product.pk]
    # find a list with all the reviews and the users that wrote those reviews
    product.reviews = [{"user": User(x.user_id), "review_text": x.review_text} for x in ratings if x.product_id_id == product.pk]
    # if ratings were found, then calculate average_rating for the current product
    if len(product_ratings) != 0:
        # convert decimal to 1 digit after point: https://stackoverflow.com/a/455634
        product.average_rating = "{:.1f}".format(sum(product_ratings) / len(product_ratings))
        for item in range(round(float(product.average_rating))):
            product.rating_classes.append("active")
        for item in range(5 - round(float(product.average_rating))):
            product.rating_classes.append("inactive")

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
