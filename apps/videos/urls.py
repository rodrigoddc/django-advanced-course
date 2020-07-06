from django.urls import path
from .views import render_video

app_name = 'videos'
urlpatterns = [
    path('<slug:slug>/', render_video, name='render_video')
]
