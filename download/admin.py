from django.contrib import admin

from download.models import AudioTrack, VideoLoad


@admin.register(AudioTrack)
class AudioTrackAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoLoad)
class VideoLoadAdmin(admin.ModelAdmin):
    pass
