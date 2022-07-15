from factory import Factory, Faker

from ..models import Apartments


class ApartmentsFactory(Factory):
    id = Faker('1')
    id_program = Faker('2')
    name = Faker('apartment')
    surface = Faker("50.0")
    number_of_pieces = Faker('3')
    features = Faker("text")

    class Meta:
        model = Apartments
