from pypro.django_assertions import assert_contains


def test_modules_title(response, modules):
    for module in modules:
        assert_contains(response, module.title)


def test_modules_link(response, modules):
    for module in modules:
        assert_contains(response, module.get_absolute_url())
