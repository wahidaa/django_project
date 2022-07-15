from rest_framework.serializers import ModelSerializer

from .models import Apartments


class ApartmentSerializer(ModelSerializer):

    class Meta:
        model = Apartments
        fields = (
            'id', 'id_program', 'name', 'surface', 'number_of_pieces', 'features'
        )
