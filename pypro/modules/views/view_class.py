from django.shortcuts import render

from pypro.modules import facade


def detail_class(request, slug):
    module = facade.find_module(slug)
    return render(request, 'modules/class_detail.html', context={'module': module})
