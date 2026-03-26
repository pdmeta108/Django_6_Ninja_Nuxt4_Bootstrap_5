from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Municipality, Parish
from .forms import PersonForm
from django.http import JsonResponse

def home(request):
    """
    Display the home page listing all Person records.

    Args:
        request (HttpRequest): The incoming HTTP request

    Returns:
        HttpResponse: Rendered template with all Person objects
    """
    people = Person.objects.all()
    context = {
        'people': people,
        'message': '¡Hello Django 6 Person CRUD!',
    }
    return render(request, 'person/home.html', context)

def create_person(request):
    """
    Handle Person creation through a form.

    GET: Displays an empty form for creating a new Person
    POST: Processes the submitted form and creates a new Person

    Args:
        request (HttpRequest): The incoming HTTP request

    Returns:
        HttpResponse: Rendered form template (GET) or redirect to home (POST)
    """
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person:home')
    else:
        form = PersonForm()

    context = {'form': form}
    return render(request, 'person/create.html', context)

def detail_person(request, pk):
    """
    Display detailed view of a specific Person.

    Args:
        request (HttpRequest): The incoming HTTP request
        pk (int): Primary key of the Person to display

    Returns:
        HttpResponse: Rendered detail template
    """
    person = get_object_or_404(Person, pk=pk)
    context = {'person': person}
    return render(request, 'person/detail.html', context)

def update_person(request, pk):
    """
    Handle Person updates through a form.

    GET: Displays a form pre-populated with Person data
    POST: Processes the submitted form and updates the Person

    Args:
        request (HttpRequest): The incoming HTTP request
        pk (int): Primary key of the Person to update

    Returns:
        HttpResponse: Rendered form template (GET) or redirect to detail view (POST)
    """
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person:detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)

    context = {'form': form, 'person': person}
    return render(request, 'person/update.html', context)

def delete_person(request, pk):
    """
    Handle Person deletion with confirmation.

    GET: Displays confirmation page
    POST: Deletes the specified Person

    Args:
        request (HttpRequest): The incoming HTTP request
        pk (int): Primary key of the Person to delete

    Returns:
        HttpResponse: Rendered confirmation template (GET) or redirect to home (POST)
    """
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person:home')

    context = {'person': person}
    return render(request, 'person/delete.html', context)

def load_municipalities(request):
    """Cargar lista de municipios de acuerdo al estado

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request

    Returns
    -------
    JsonResponse (list | empty_list)
        Lista de municipios pertenecientes al estado
    """
    estate_id = request.GET.get('estate_id')

    # Si estate_id es None, una cadena vacía o no es un dígito
    if not estate_id or estate_id == "":
        return JsonResponse([], safe=False)

    # Obtener los municipios correspondientes al id del estado y ordenar por orden alfabetico
    municipalities = Municipality.objects.filter(estate_id=estate_id).order_by('name')
    return JsonResponse(list(municipalities.values('code', 'name')), safe=False)

def load_parishes(request):
    """Cargar lista de parroquias de acuerdo al municipio

    Parameters
    ----------
    request : HttpRequest
        The incoming HTTP request

    Returns
    -------
    JsonResponse (list | empty_list)
        Lista de parroquias pertenecientes al municipio
    """
    municipality_id = request.GET.get('municipality_id')

    # Si municipality_id es None, una cadena vacía o no es un dígito
    if not municipality_id or municipality_id == "":
        return JsonResponse([], safe=False)

    # Obtener los municipios correspondientes al id del estado y ordenar por orden alfabetico
    parishes = Parish.objects.filter(municipality_id=municipality_id).order_by('name')
    return JsonResponse(list(parishes.values('code', 'name')), safe=False)
