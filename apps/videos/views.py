from django.shortcuts import render


def render_video(request, slug):
    return render(request, 'videos/video.html')
