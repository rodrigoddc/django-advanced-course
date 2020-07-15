

from pypro.django_assertions import assert_contains
from pypro.modules.models import Module


def test_modules_title(response_module_detail, module):
    assert_contains(response_module_detail, module.title)


def test_modules_link(response_module_detail, module: Module):
    assert_contains(response_module_detail, module.get_absolute_url())


def test_modules_description(response_module_detail, module: Module):
    assert_contains(response_module_detail, module.description)


def test_modules_audience(response_module_detail, module: Module):
    assert_contains(response_module_detail, module.audience)
