from django.shortcuts import render
from .models import Project


def home(request):
    projects_left = Project.objects.all()[:10]  # Get projects 1 to 10
    projects_right = Project.objects.all()[10:20]  # Get projects 11 to 20
    return render(request, 'portfolio_website/home.html', {
        'projects_left': projects_left,
        'projects_right': projects_right
    })


def contact(request):
    return render(request, 'portfolio_website/contact.html')