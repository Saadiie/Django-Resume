from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def home_view(request):
    return render(request, 'pages/home.html')


def about_view(request):
    return render(request, 'pages/about.html')


def contact_view(request):

    success = False

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'New Contact Message from {name}',

                message=(
                    f'Name: {name}\n'
                    f'Phone: {phone_number}\n'
                    f'Email: {email}\n\n'
                    f'Message:\n{message}'
                ),

                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            success = True

            # Clear form after successful submission
            form = ContactForm()

    else:
        form = ContactForm()

    return render(
        request,
        'pages/contact.html',
        {
            'form': form,
            'success': success
        }
    )