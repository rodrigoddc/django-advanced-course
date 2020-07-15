from pypro.modules import facade


def modules_list(request):
    return {
        'MODULES': facade.modules_sorted_by_order()
    }
