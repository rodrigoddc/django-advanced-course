from django.shortcuts import render

from pypro.modules.models.model_class import Lecture


def lecture_detail(request, slug):
    lecture = Lecture.objects.get(slug=slug)
    return render(request, 'modules/lecture_detail.html', context={'lecture': lecture})
