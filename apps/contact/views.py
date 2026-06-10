from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            try:
                send_mail(
                    subject=f'[Stunt Bike Extreme] {msg.subject}',
                    message=f'From: {msg.name} <{msg.email}>\n\n{msg.message}',
                    from_email=settings.ADMIN_EMAIL,
                    recipient_list=[settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
        'page_title': 'Contact Us — Stunt Bike Extreme',
        'meta_description': 'Get in touch with the Stunt Bike Extreme team. Send us your questions or feedback.',
    })


def contact_success(request):
    return render(request, 'contact/success.html', {
        'page_title': 'Message Sent — Stunt Bike Extreme',
    })
