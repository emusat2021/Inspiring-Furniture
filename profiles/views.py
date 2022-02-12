from django.shortcuts import render, get_list_or_404

from profiles.models import UserProfile


def profile(request):
    """ Display the user's profile. """

    profile = get_list_or_404(UserProfile, user=request.user)
    
    template = 'profiles/profile.html'
    context = {
def order_history(request, order_number):
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