from django.db import models


class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    is_actif = models.BooleanField()
    promo_code = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Apartments(models.Model):
    id = models.IntegerField(primary_key=True)
    id_program = models.ForeignKey("Program", null=False, on_delete=models.CASCADE, related_name="prog")
    name = models.CharField(max_length=255)
    surface = models.FloatField()
    number_of_pieces = models.IntegerField()
    features = models.TextField(blank=True)

    def __str__(self):
        return self.name
