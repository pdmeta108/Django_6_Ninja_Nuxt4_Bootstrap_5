from django.shortcuts import render
from models import Estate

def home(request):
    """
    Display the home page listing all Estate records.

    Args:
        request (HttpRequest): The incoming HTTP request

    Returns:
        HttpResponse: Rendered template with all Estate objects
    """
    estates = Estate.objects.all()
    context = {
        'estates': estates,
        'message': '¡Hello Django 6 Estate CRUD!',
    }
    return render(request, 'estate/home.html', context)
