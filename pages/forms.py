from django import forms

class ContactForm(forms.Form):
    name         = forms.CharField(max_length=100, label='Full Name')
    phone_number = forms.CharField(max_length=20,  label='Phone Number')
    email        = forms.EmailField(label='Email Address')
    message      = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), label='Message')