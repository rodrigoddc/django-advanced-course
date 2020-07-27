

from pypro.django_assertions import assert_contains
from pypro.modules.models.model_lecture import Lecture


def test_lecture_title(response_lecture_detail, lecture):
    assert_contains(response_lecture_detail, lecture.title)


def test_lectures_title(response_list, lectures):
    for lecture in lectures:
        assert_contains(response_list, lecture.title)


def test_lecture_module_breadcumb(response_lecture_detail, lecture: Lecture):
    assert_contains(response_lecture_detail, f'<li class="breadcrumb-item"><a href="'
                                             f'{ lecture.module.get_absolute_url() }'
                                             f'"> { lecture.module.title }</a></li>')
