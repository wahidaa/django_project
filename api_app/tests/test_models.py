from django.test import TestCase

from ..models import Apartments
from .factories import ApartmentsFactory


class ApartmentTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        apartment = ApartmentsFactory()
        self.assertEqual(str(apartment), apartment.name)
