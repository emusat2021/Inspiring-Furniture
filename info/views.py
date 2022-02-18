from django.shortcuts import render


def info(request):
    """ Information table of contents """
    template = 'info/info.html'
    context = {}

    return render(request, template, context)


def about_us(request):
    """ Information about the company """
    template = 'info/about_us.html'
    context = {}

    return render(request, template, context)

def how_to_buy(request):
    """ Information regarding how to buy products """
    template = 'info/how_to_buy.html'
    context = {}

    return render(request, template, context)
