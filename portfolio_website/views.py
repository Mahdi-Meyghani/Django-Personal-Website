from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .models import Project
from . import forms
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def home(request):
    projects_left = Project.objects.all()[:10]  # Get projects 1 to 10
    projects_right = Project.objects.all()[10:20]  # Get projects 11 to 20
    return render(request, 'portfolio_website/home.html', {
        'projects_left': projects_left,
        'projects_right': projects_right
    })


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        try:
            validate_email(email)
            body = f"From: {email}\n\n{name.title()}\n{message}"
            email_message = EmailMessage(
                subject='Portfolio Django Website Email',
                body=body,
                to=['portfolio.websate@gmail.com'],
            )
            email_message.send()
            messages.success(request, 'Your email has been sent successfully. Thanks 😄')
            return redirect('contact')
        except ValidationError:
            messages.error(request, 'Invalid email address. 😣')
        except Exception:
            messages.error(request, 'Failed to send email. Try again. 😢')

    return render(request, 'portfolio_website/contact.html')
