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
    form = ContactForm()
    print(form)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name         = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            email        = form.cleaned_data['email']
            message      = form.cleaned_data['message']

            send_mail(
                subject=f'New Contact Message from {name}',
                message=f'Name: {name}\nPhone: {phone_number}\nEmail: {email}\n\nMessage:\n{message}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            success = True
            form = ContactForm()  # clear form after success

    return render(request, 'pages/contact.html', {'form': form, 'success': success})