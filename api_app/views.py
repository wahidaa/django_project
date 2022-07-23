from .models import Apartments
from .models import Program
from django.db.models import Q
from django.db.models import F
from datetime import datetime

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from .serializers import ProramSerializer
from .serializers import ApartmentSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def all_apartments(request):
    task = Apartments.objects.all()
    task_serializer = ApartmentSerializer(task, many=True)
    return JSONResponse(task_serializer.data)


@csrf_exempt
def all_programs(request):
    task = Program.objects.all()
    task_serializer = ProramSerializer(task, many=True)
    return JSONResponse(task_serializer.data)


def list_apartments_with_actif_program(request):
    program_ids = list(Program.objects.filter(is_actif=True).only('id'))
    print(program_ids)
    apartments = Apartments.objects.filter(id_program__in=program_ids)
    task_serializer = ApartmentSerializer(apartments, many=True)
    return JSONResponse(task_serializer.data)


def list_apartments_between_two_prices(request):
    program_ids = Program.objects.filter(Q(price__gte=100000) & Q(price__lte=180000)).only('id')
    apartments = Apartments.objects.filter(id_program__in=program_ids)
    task_serializer = ApartmentSerializer(apartments, many=True)
    return JSONResponse(task_serializer.data)


def list_programs_with_pool(request):
    program_ids = Apartments.objects.filter(features__contains='piscine').only('program_id')
    programs = Program.objects.filter(id__in=program_ids)
    task_serializers = ProramSerializer(programs, many=True)
    return JSONResponse(task_serializers.data)


def list_apartments_with_promo_code(request, promo_code):
    apartments = []
    if promo_code == 'PERENOEL':
        Program.objects.all().update(price=F('price') * 0.05)
        Program.objects.all().update(name='PROMO SPECIALE')
        apartments = Apartments.objects.all()
    task_serializers = ApartmentSerializer(apartments, many=True)
    return JSONResponse(task_serializers.data)


def sorted_apartments_list(request):
    current_month = datetime.now().month
    if current_month == 12 or (3 >= current_month >= 1):
        apartments1 = list(Apartments.objects.filter(features__contains='proches des stations de ski'))
        apartment_ids = [a['id'] for a in apartments1]
        apartments2 = list(Apartments.objects.exclude(id__in=apartment_ids).order_by('-price').order_by('-surface'))
        apartments = apartments1 + apartments2
    elif 9 >= current_month >= 6:
        apartments1 = list(Apartments.objects.filter(features__contains='piscine'))
        apartment_ids = [a['id'] for a in apartments1]
        apartments2 = list(Apartments.objects.exclude(id__in=apartment_ids).order_by('-price').order_by('-surface'))
        apartments = apartments1 + apartments2
    else:
        apartments = list(Apartments.objects.all().order_by('-price').order_by('-surface'))

    task_serializers = ApartmentSerializer(apartments, many=True)
    return JSONResponse(task_serializers.data)
