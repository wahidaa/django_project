from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import ApartmentViewSet


router = DefaultRouter()
router.register(r'apartment', ApartmentViewSet, 'apartment')

urlpatterns = [
    re_path('^', include(router.urls)),
]