from django.contrib import admin

from apps.videos.models.model_video import Video


class VideoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Video, VideoAdmin)
