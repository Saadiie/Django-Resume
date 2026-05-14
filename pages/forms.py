from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

    # Email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith("@gmail.com"):
            raise forms.ValidationError(
                "Only Gmail addresses are allowed."
            )

        return email

    # Phone number validation
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        pattern = r'^\+?\d{10,15}$'

        if not re.match(pattern, phone):
            raise forms.ValidationError(
                "Enter a valid phone number."
            )

        return phone

    # Name validation
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if len(name) < 2:
            raise forms.ValidationError(
                "Name must be at least 2 characters long."
            )

        return name