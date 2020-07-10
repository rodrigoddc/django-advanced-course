import pytest
from django.urls import reverse


@pytest.fixture
def response(client):
    response = client.get(reverse('base:home'))
    return response
