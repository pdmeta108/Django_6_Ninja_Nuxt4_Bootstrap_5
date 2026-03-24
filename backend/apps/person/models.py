from django.db import models

class Estate(models.Model):
    """Representación del modelo Estate (Estado) en el sistema

    Parameters
    ----------
    models : _type_
        _description_
    """

    # Estate fields
    name = models.CharField(max_length=100)
    code = models.PositiveIntegerField()

    def __str__(self):
        """
        String representation of the Estate model.

        Returns:
            str: The estate's name for easy identification in admin and queries.
        """
        return self.name

class Municipality(models.Model):
    """Representación del modelo Municipality (Municipio) en el sistema

    Parameters
    ----------
    models : _type_
        _description_
    """

    # Municipality fields
    name = models.CharField(max_length=100)
    code = models.PositiveIntegerField()
    estate = models.ForeignKey(
        Estate,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="municipality_estates"
    )

    def __str__(self):
        """
        String representation of the Municipality model.

        Returns:
            str: The municipality's name for easy identification in admin and queries.
        """
        return self.name

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
        related_name="person_estates"
    )
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="person_municipalities"
    )

    def __str__(self):
        """
        String representation of the Person model.

        Returns:
            str: The person's name for easy identification in admin and queries.
        """
        return self.name
