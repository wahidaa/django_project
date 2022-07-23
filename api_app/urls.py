from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

router = DefaultRouter()

urlpatterns = [
    path('all_apartments/', views.all_apartments, name='all_apartments'),
    path('all_programs/', views.all_programs, name='all_programs'),
    path('list_apartments_with_actif_program/', views.list_apartments_with_actif_program,
         name='list_apartments_with_actif_program'),
    path('list_apartments_between_two_prices/', views.list_apartments_between_two_prices,
         name='list_apartments_between_two_prices'),
    path('list_programs_with_pool/', views.list_programs_with_pool,
         name='list_programs_with_pool'),
    path('list_apartments_with_promo_code/<str:promo_code>', views.list_apartments_with_promo_code,
         name='list_apartments_with_promo_code'),
    path('sorted_apartments_list', views.sorted_apartments_list,
         name='sorted_apartments_list'),

]
