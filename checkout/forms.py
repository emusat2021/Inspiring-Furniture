from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
        # validate full_name to contain only letters
        # https://stackoverflow.com/a/15472787
        self.fields['full_name'].widget.attrs['pattern'] = '^[a-zA-Z_ ]*$'
        # https://stackoverflow.com/a/47600422
        self.fields['full_name'].widget.attrs['oninvalid'] = "setCustomValidity('Name must contain only letters and/or space.')"
        # validate phone number to contain only numbers and the plus sign
        self.fields['phone_number'].widget.attrs['pattern'] = '[0-9\+]+'
        self.fields['phone_number'].widget.attrs['oninvalid'] = "setCustomValidity('Telephone number must contain only digits and/or plus. No other characters are allowed.')"
