from django.urls import path

from pypro.modules.views.view_module import module_detail, module_list
from pypro.modules.views.view_lecture import lecture_detail

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', module_detail, name='module_detail'),
    path('list/', module_list, name='module_list'),
    path('lecture/<slug:slug>', lecture_detail, name='lecture_detail'),
]
