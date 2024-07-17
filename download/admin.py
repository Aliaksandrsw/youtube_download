from django.contrib import admin

from download.models import AudioTrack


@admin.register(AudioTrack)
class AudioTrackAdmin(admin.ModelAdmin):
    pass

