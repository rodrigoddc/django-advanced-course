from pypro.django_assertions import assert_contains
from pypro.modules.models.model_module import Module


def test_modules_title(response_modules_list, module):
    assert response_modules_list.status_code == 200
#
# def test_modules_link(response_list, module: Module):
#     assert_contains(response_list, module.get_absolute_url())
#
#
# def test_modules_description(response_list, module: Module):
#     assert_contains(response_list, module.description)
#
#
# def test_modules_audience(response_list, module: Module):
#     assert_contains(response_list, module.audience)
#
#
# def test_lectures_links(response_list, lectures):
#     for lecture in lectures:
#         assert_contains(response_list, lecture.get_absolute_url())
