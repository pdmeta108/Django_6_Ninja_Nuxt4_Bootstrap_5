from django.urls import path
from . import views

# Define the application namespace for URL reversing
# This helps distinguish URLs between different apps when using 'url' template tag
app_name = 'estate'

# URL patterns for the Estate CRUD (Create, Read, Update, Delete) operations
urlpatterns = [
    # Home/List view: Displays all estate records
    # URL: /
    # View: home - Shows listing of all estates
    path('', views.home, name='home'),
]
