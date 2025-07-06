from django.db import models
from django.core.exceptions import ValidationError
import phonenumbers

def validate_international_phone_number(value):
    """
    Validates that the phone number is a valid international number.
    """
    try:
        parsed_number = phonenumbers.parse(value, "BR")
        if not phonenumbers.is_valid_number(parsed_number):
            raise ValidationError("Please enter a valid international phone number (e.g., +5531999999999).")
    except phonenumbers.phonenumberutil.NumberParseException as e:
        raise ValidationError(f"Invalid phone number format: {e}")

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.CharField(max_length=20, null=True, blank=True, validators=[validate_international_phone_number])
  joined_date = models.DateField(null=True, blank=True)
  email = models.EmailField(null=True, blank=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"
