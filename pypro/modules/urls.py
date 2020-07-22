from django.urls import path

from pypro.modules.views.view_module import module_detail
from pypro.modules.views.view_lecture import lecture_detail

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', module_detail, name='module_detail'),
    path('lecture/<slug:slug>', lecture_detail, name='lecture_detail'),
]
