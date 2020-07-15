from django.urls import path

from pypro.modules.views.view_module import detail_module
from pypro.modules.views.view_class import detail_class

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', detail_module, name='module_detail'),
    path('<slug:slug>', detail_class, name='class_detail'),
]
