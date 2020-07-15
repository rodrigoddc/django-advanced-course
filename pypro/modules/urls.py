from django.urls import path

from pypro.modules.views import detail

app_name = 'modules'
urlpatterns = [
    path('<slug:slug>', detail, name='detail'),
]
