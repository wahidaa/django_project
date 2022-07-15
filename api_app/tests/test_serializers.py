from django.test import TestCase

from ..serializers import ApartmentSerializer
from .factories import ApartmentsFactory


class ApartmentSerializer(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        company = ApartmentsFactory()
        serializer = ApartmentSerializer()
        for field_name in [
            'id', 'id_program', 'name', 'surface', 'number_of_pieces', 'features'
        ]:
            self.assertEqual(
                serializer.data[field_name],
                getattr(company, field_name)
            )