from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'base/home.html'


def home(request):
    return render(request, template_name='base/home.html')
