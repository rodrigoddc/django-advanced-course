from django.shortcuts import render, get_object_or_404

from apps.videos.models.model_video import Video


def video_list(request):
    videos = Video.objects.order_by('created_at').all()
    return render(request, 'videos/list_videos.html', context={'videos': videos})


def video_render(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'videos/video.html', context={'video': video})
