from pypro.django_assertions import assert_contains


def test_modules_title(response_modules, modules):
    for module in modules:
        assert_contains(response_modules, module.title)


def test_modules_link(response_modules, modules):
    for module in modules:
        assert_contains(response_modules, module.get_absolute_url())
