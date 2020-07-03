from django.urls import path
from .views import Home, home

app_name = 'base'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('home/', home, name='test_home')
]
