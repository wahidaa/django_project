from rest_framework.serializers import ModelSerializer

from .models import Apartments
from .models import Program


class ApartmentSerializer(ModelSerializer):
    class Meta:
        model = Apartments
        fields = (
            'id', 'id_program', 'name', 'surface', 'number_of_pieces', 'features'
        )


class ProramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = (
            'name', 'is_actif', 'price'
        )
