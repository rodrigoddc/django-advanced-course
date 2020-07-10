from django.urls import reverse

from pypro.django_assertions import assert_contains


def test_status_code(response):
    assert response.status_code == 200


def test_home_title(response):
    assert_contains(response, '<title> Home | Pypro </title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("base:home")}">Home')
