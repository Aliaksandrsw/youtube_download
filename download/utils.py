import os

from .models import AudioTrack, VideoLoad
from django.core.files.base import ContentFile
import yt_dlp
from django.core.files import File
from django.db import transaction


def download_audio(youtube_url):
    existing_audio = AudioTrack.objects.filter(youtube_url=youtube_url).first()
    if existing_audio:
        return existing_audio

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = ydl.prepare_filename(info)
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}.mp3"

        with open(new_filename, 'rb') as f:
            audio_content = f.read()

        audio_track = AudioTrack(
            title=info['title'],
            youtube_url=youtube_url
        )
        audio_track.audio_file.save(new_filename, ContentFile(audio_content))
        audio_track.save()

        os.remove(new_filename)

    return audio_track


def download_video(youtube_url):
    existing_video = VideoLoad.objects.filter(youtube_url=youtube_url).first()
    if existing_video:
        return existing_video

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = ydl.prepare_filename(info)
        base, ext = os.path.splitext(filename)
        new_filename = f"{base}.mp4"

        if os.path.exists(filename) and filename != new_filename:
            os.rename(filename, new_filename)

        with transaction.atomic():
            video = VideoLoad(
                title=info['title'],
                youtube_url=youtube_url
            )
            with open(new_filename, 'rb') as f:
                video.video_file.save(new_filename, File(f), save=False)
            video.save()

        os.remove(new_filename)

        return video
