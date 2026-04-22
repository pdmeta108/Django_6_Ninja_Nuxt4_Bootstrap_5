from django.db import models
from apps.estate.models import Estate, Municipality, Parish

class Person(models.Model):
    """
    Represents a person in the system.

    This model stores basic information about individuals including their name,
    email, age, and timestamps for record creation and updates.
    """

    # Personal Information Fields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    estate = models.ForeignKey(
        Estate,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="estate_persons"
    )
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="municipality_persons"
    )
    parish = models.ForeignKey(
        Parish,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="parish_persons"
    )

    def __str__(self):
        """
        String representation of the Person model.

        Returns:
            str: The person's name for easy identification in admin and queries.
        """
        return self.name
