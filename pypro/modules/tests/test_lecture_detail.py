

from pypro.django_assertions import assert_contains


def test_class_title(response_lecture_detail, lecture):
    assert_contains(response_lecture_detail, lecture.title)


def test_classes_title(response_list, lectures):
    for x in lectures:
        assert_contains(response_list, x.title)
