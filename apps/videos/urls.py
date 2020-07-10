from django.urls import path
from .views import video_render, video_list

app_name = 'videos'
urlpatterns = [
    path('', video_list, name='video_list'),
    path('<slug:slug>/', video_render, name='video_render'),
]
