from pypro.modules.models.model_module import Module


def find_module(slug: str) -> Module:
    return Module.objects.get(slug=slug)


def modules_sorted_by_order() -> object:
    """
    List modules sorted by title
    :return: Modules sorted by 'order' column
    """

    return list(Module.objects.order_by('order').all())
