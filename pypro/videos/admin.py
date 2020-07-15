from django.contrib import admin

from pypro.videos.models.model_video import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'vimeo_id', 'created_at', 'id')
    ordering = ('created_at',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Video, VideoAdmin)
