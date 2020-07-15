from typing import List

from .models.model_modules import Module


def modules_sorted_by_title() -> object:
    """
    List modules sorted by title
    :return: Modules sorted by 'order' column
    """

    return list(Module.objects.order_by('title').all())


def modules_sorted_by_order() -> object:
    """
    List modules sorted by title
    :return: Modules sorted by 'order' column
    """

    return list(Module.objects.order_by('order').all())


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)
