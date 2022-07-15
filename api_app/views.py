from .models import Apartments
from .models import Program
from django.db.models import Q
from django.db.models import F
from datetime import datetime


def list_apartments_with_actif_program(request):
    program_ids = list(Program.objects.filter(is_actif=True).only('id'))
    apartments = list(Apartments.objects.filter(program_id__in=program_ids))
    return apartments


def list_apartments_between_two_prices(request):
    apartments = list(Apartments.objects.filter(
        Q(price__gte=100000) | Q(price__lte=180000)
    ))
    return apartments


def list_programs_with_pool(request):
    program_ids = list(Apartments.objects.filter(features__contains='piscine').only('program_id'))
    programs = list(Program.objects.filter(id__in=program_ids))
    return programs


def list_apartments_with_promo_code(request, promo_code):
    apartments = []
    if promo_code == 'PERE NOEL':
        program_ids = list(Program.objects.annotate(
            price=F('price') * 0.05).annotate(name='PROMO SPECIALE').only(id))
        apartments = list(Apartments.objects.filter(program_id__in=program_ids))
    return apartments


def sorted_apartments_list(promo_code):
    current_month = datetime.now().month
    if current_month == 12 or (current_month <= 3 and current_month >= 1):
        apartments1 = list(Apartments.objects.filter(features__contain='proches des stations de ski'))
        apartment_ids = [a['id'] for a in apartments1]
        apartments2 = list(Apartments.objects.filter(id__nin=apartment_ids).order_by('-price').order_by('-surface'))
        apartments = apartments1 + apartments2
    elif current_month <= 9 and current_month >= 6:
        apartments1 = list(Apartments.objects.filter(features__contain='qui ont une piscine'))
        apartment_ids = [a['id'] for a in apartments1]
        apartments2 = list(Apartments.objects.filter(id__nin=apartment_ids).order_by('-price').order_by('-surface'))
        apartments = apartments1 + apartments2
    else:
        apartments = list(Apartments.objects.all().order_by('-price').order_by('-surface'))

    return apartments
