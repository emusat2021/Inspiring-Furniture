from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False
        # validate default_full_name to contain only letters
        # https://stackoverflow.com/a/15472787
        self.fields['default_full_name'].widget.attrs['pattern'] = '^[a-zA-Z_ ]*$'
        # https://stackoverflow.com/a/47600422
        self.fields['default_full_name'].widget.attrs['oninvalid'] = "setCustomValidity('Name must contain only letters and/or space.')"
        # validate phone number to contain only numbers and the plus sign
        self.fields['default_phone_number'].widget.attrs['pattern'] = '[0-9\+]+'
        self.fields['default_phone_number'].widget.attrs['oninvalid'] = "setCustomValidity('Telephone number must contain only digits and/or plus. No other characters are allowed.')"
