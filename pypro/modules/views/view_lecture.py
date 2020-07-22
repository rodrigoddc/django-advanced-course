from django.shortcuts import render

from pypro.modules.facades import facade_lecture


def lecture_detail(request, slug):
    lecture = facade_lecture.find_lecture(slug)
    return render(request, 'modules/lecture_detail.html', context={'lecture': lecture})
