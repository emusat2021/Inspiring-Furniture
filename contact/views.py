from django.shortcuts import render


def contact(request):
    """
    A view to return contact page and render the form, allowing a user
    to contact the website owner/manager by submitting the form.
    """

    return render(request, 'contact/contact.html')


def contact_thankyou(request):
    """
    A view to return contact_thankyou page in order \
        to inform user that the message was succseddfully sent
    """
    return render(request, 'contact/contact_thankyou.html')