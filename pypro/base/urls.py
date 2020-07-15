from django.urls import path
from .views import Home

app_name = 'base'
urlpatterns = [
    path('', Home.as_view(), name='home'),
]
