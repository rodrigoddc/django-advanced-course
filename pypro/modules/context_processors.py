from pypro.modules.facades import facade_module


def modules_list(request):
    return {
        'MODULES': facade_module.modules_sorted_by_order()
    }
