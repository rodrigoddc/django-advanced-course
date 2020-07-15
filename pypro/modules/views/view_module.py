from django.shortcuts import render

from pypro.modules import facade


def module_detail(request, slug):
    module = facade.find_module(slug)
    lectures = facade.list_class_by_module(module)
    return render(request, 'modules/module_detail.html', {'module': module, 'lectures': lectures})
