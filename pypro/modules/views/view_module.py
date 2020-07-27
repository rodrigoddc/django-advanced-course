from django.shortcuts import render

import pypro.modules.facades.facade_lecture
from pypro.modules.facades import facade_module


def module_detail(request, slug):
    module = facade_module.find_module(slug)
    lectures = pypro.modules.facades.facade_lecture.list_lecture_by_module(module)
    return render(request, 'modules/module_detail.html', {'module': module, 'lectures': lectures})


def module_list(request):
    modules = facade_module.modules_sorted_by_order()
    return render(request, 'modules/module_list.html', {'modules': modules})
