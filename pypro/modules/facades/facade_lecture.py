from pypro.modules.models.model_module import Module
from pypro.modules.models.model_lecture import Lecture


def find_lecture(slug: str) -> Lecture:
    return Lecture.objects.select_related('module').get(slug=slug)


def list_lecture_by_module(module: Module):
    return list(module.lecture_set.order_by('order').all())
