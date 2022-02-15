# Taken from: https://github.com/irinatu17/Art-of-Tea
# Taken from: https://github.com/juanstelling/MS4-prints
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """
    A view to return contact page and render the form, allowing a user
    to contact the website owner/manager by submitting the form.
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            try:
                send_mail(
                    f"Message from {full_name} <{user_email}>", # log line
                    "You received a contact inquery", # message
                    settings.EMAIL_HOST_USER,  # to
                    [settings.DEFAULT_FROM_EMAIL], # from
                    fail_silently=False
                )
                messages.info(request, 'Your message has been received. We will contact you as soon as possible!')
                return redirect('home')
            except BadHeaderError as e:
                messages.error(request, (e))
                return redirect(reverse('contact'))
        else:
            msg = 'Sorry, invalid fields found in contact form. Please try again.'
            messages.error(request, (msg))
            return redirect(reverse('home'))

    else:
        # Attempt to profile full_name and email fields for logged in user, if they have
        # this information saved in the profile
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            user_email = profile.user.email
            contact_form = ContactForm(initial={
                'full_name': profile.default_full_name,
                'email': user_email,
                })
        else:
            contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
