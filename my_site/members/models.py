"""Module to define the Member model for the members app."""

import phonenumbers
from django.core.exceptions import ValidationError
from django.db import models


def validate_international_phone_number(value: str) -> None:
    """Validate if the phone number is a valid international number."""
    try:
        parsed_number = phonenumbers.parse(value, "BR")
        if not phonenumbers.is_valid_number(parsed_number):
            message = (
                "The phone number is not valid. "
                "Please enter a valid international phone number."
                "Example: +5511999999999 (Brazil)"
            )
            raise ValidationError(message)
    except phonenumbers.phonenumberutil.NumberParseException as err:
        e = f"The phone number '{value}' raised an error: {err}"
        raise ValidationError(e) from err


class Member(models.Model):
    """Model to represent a member of the members app."""

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=20,
        default=None,
        null=False,
        blank=False,
        validators=[validate_international_phone_number],
    )
    joined_date = models.DateField(default=None)
    email = models.EmailField(default=None)

    def __str__(self) -> str:
        """Return a string representation of the member."""
        return f"{self.firstname} {self.lastname}"
