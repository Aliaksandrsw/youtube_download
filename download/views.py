from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, DetailView
from .forms import YouTubeURLForm
from .models import AudioTrack, VideoLoad
from .utils import download_audio, download_video


class DownloadYouTubeView(FormView):
    template_name = 'download/index.html'
    form_class = YouTubeURLForm

    def form_valid(self, form):
        youtube_url = form.cleaned_data['youtube_url']
        download_type = form.cleaned_data['download_type']

        if download_type == 'audio':
            audio = download_audio(youtube_url)
            return redirect('audio_detail', slug=audio.slug)
        else:

            video = download_video(youtube_url)
            return redirect('video_detail', slug=video.slug)


class AudioDetailView(DetailView):
    model = AudioTrack
    template_name = 'download/audio_detail.html'
    context_object_name = 'audio'


class VideoDetailView(DetailView):
    model = VideoLoad
    template_name = 'download/video_detail.html'
    context_object_name = 'video'
