from django import forms
from .models import Person, Estate, Municipality

class PersonForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Person instances.

    This form handles the validation and presentation of Person data,
    providing a secure interface for person-related operations in views.
    Automatically generated from the Person model with configurable fields.
    """
    estate = forms.ModelChoiceField(queryset=Estate.objects.all(), empty_label=" * Selecciones un estado * ")
    municipality = forms.ModelChoiceField(queryset=Municipality.objects.all(), empty_label=" * Seleccione un municipio * ")

    class Meta:
        """
        Metadata class defining the form's relationship to the model.

        Attributes:
            model (Model): The Django model class this form is based on
            fields (list): The model fields to include in the form
            labels (dict): Custom display labels for form fields
            help_texts (dict): Descriptive help text for each field
            error_messages (dict): Custom error messages
            widgets (dict): Custom widgets for field rendering
        """
        model = Person

        fields = [
            'name',
            'email',
            'age',
            'estate',
            'municipality',
            'parish',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Always allow all municipalities
        self.fields['municipality'].queryset = Municipality.objects.all()
        self.fields['municipality'].choices = [
            ("", " * Seleccione un municipio * ")
        ]

        # Check if we are updating (instance exists and has a PK)
        if self.instance and self.instance.pk:
            # Access the estate object or its ID
            current_estate_id = self.instance.estate_id
            specific_municipalities = Municipality.objects.filter(estate_id=current_estate_id)
            # Show municipalities by state
            self.fields['municipality'].choices = [
                (e.pk, str(e)) for e in specific_municipalities.distinct()
            ]
