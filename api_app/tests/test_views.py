import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from ..models import Apartments, Program
from django.urls import reverse


class RouteTest(TestCase):
    @pytest.mark.django_db
    def test_get_all_apartments(self):
        homepage_url = reverse("api_app/all_apartments")
        response = self.client.get(homepage_url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_list_apartments_with_actif_program(self):
        homepage_url = reverse("api_app/list_apartments_with_actif_program")
        response = self.client.get(homepage_url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_list_apartments_between_two_prices(self):
        homepage_url = reverse("api_app/list_apartments_between_two_prices")
        response = self.client.get(homepage_url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_list_programs_with_pool(self):
        homepage_url = reverse("api_app/list_programs_with_pool")
        response = self.client.get(homepage_url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_list_apartments_with_promo_code(self):
        homepage_url = reverse("api_app/list_apartments_with_promo_code/PERENOEL")
        response = self.client.get(homepage_url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def sorted_apartments_list(self):
        homepage_url = reverse("api_app/sorted_apartments_list")
        response = self.client.get(homepage_url)
        assert response.status_code == 200