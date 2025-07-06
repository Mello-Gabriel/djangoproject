from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Member

class MemberModelTest(TestCase):

    def test_can_create_member_with_valid_phone_number(self):
        """Tests that a Member can be created with a valid international phone number."""
        valid_phone = "+5531999363088"
        member = Member.objects.create(
            firstname="John",
            lastname="Doe",
            phone=valid_phone
        )
        self.assertEqual(member.phone, valid_phone)
        # The full_clean method is what triggers the model-level validation.
        member.full_clean()

    def test_cannot_create_member_with_invalid_phone_number(self):
        """Tests that creating a Member with an invalid phone number raises a ValidationError."""
        invalid_phone = "12345"
        member = Member(
            firstname="Jane",
            lastname="Doe",
            phone=invalid_phone
        )
        with self.assertRaises(ValidationError) as context:
            member.full_clean()
        self.assertIn('phone', context.exception.message_dict)

    def test_can_create_member_with_blank_phone_number(self):
        """Tests that a Member can be created with a blank or null phone number."""
        member_blank = Member.objects.create(
            firstname="No",
            lastname="Phone",
            phone=""
        )
        member_blank.full_clean()
        self.assertEqual(member_blank.phone, "")

        member_null = Member.objects.create(
            firstname="Null",
            lastname="Phone",
            phone=None
        )
        member_null.full_clean()
        self.assertIsNone(member_null.phone)

    def test_can_create_member_with_brazilian_local_phone_number(self):
        """Tests that a Member can be created with a valid Brazilian local phone number (without +)."""
        valid_local_phone = "31999363088"
        member = Member.objects.create(
            firstname="Local",
            lastname="Phone",
            phone=valid_local_phone
        )
        self.assertEqual(member.phone, valid_local_phone)
        member.full_clean()
