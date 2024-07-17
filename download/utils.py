from .models import AudioTrack
from django.core.files.base import ContentFile
import yt_dlp
import os


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
