# Taken from https://github.com/irinatu17/Art-of-Tea
# Taken from: https://github.com/juanstelling/MS4-prints
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    A form for contact page
    """

    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Name',
            'email': 'Email Address',
            'message': 'Message',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
        # validate default_full_name to contain only letters
        # https://stackoverflow.com/a/15472787
        self.fields['full_name'].widget.attrs['pattern'] = '^[a-zA-Z_ ]*$'
        # https://stackoverflow.com/a/47600422
        self.fields['full_name'].widget.attrs['oninvalid'] = "setCustomValidity('Name must contain only letters and/or space.')"
