import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.modules.models.model_class import Lecture
from pypro.modules.models.model_modules import Module


@pytest.fixture
def module(db):
    return baker.make(Module)


@pytest.fixture
def modules(db):
    return baker.make(Module, 3)


@pytest.fixture
def lecture(db):
    return baker.make(Lecture)


@pytest.fixture
def lectures(module):
    return baker.make(Lecture, _quantity=3, module=module)


@pytest.fixture
def response_modules(client, modules, lectures):
    return client.get(reverse('base:home'))


@pytest.fixture
def response_list(client, module, lectures):
    return client.get(reverse('modules:module_detail', kwargs={'slug': module.slug}))


@pytest.fixture
def response_module_detail(client, module):
    return client.get(reverse('modules:module_detail', kwargs={'slug': module.slug}))


@pytest.fixture
def response_lecture_detail(client, lecture):
    return client.get(reverse('modules:lecture_detail', kwargs={'slug': lecture.slug}))
