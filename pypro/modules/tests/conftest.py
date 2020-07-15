import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.modules.models.model_modules import Module


@pytest.fixture
def module(db):
    return baker.make(Module)


@pytest.fixture
def modules(db):
    return baker.make(Module, 3)


@pytest.fixture
def response(client, modules):
    return client.get(reverse('base:home'))


@pytest.fixture
def response_module_detail(client, module):
    return client.get(reverse('modules:module_detail', kwargs={'slug': module.slug}))
