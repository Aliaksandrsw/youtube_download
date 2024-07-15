from django.shortcuts import redirect, get_object_or_404
from django.views.generic import FormView, DetailView
from .forms import YouTubeURLForm
from .models import AudioTrack
from .utils import download_audio


class DownloadYouTubeAudioView(FormView):
    template_name = 'download/index.html'
    form_class = YouTubeURLForm

    def form_valid(self, form):
        youtube_url = form.cleaned_data['youtube_url']
        audio_track = download_audio(youtube_url)
        return redirect('audio_detail', slug=audio_track.slug)


class AudioDetailView(DetailView):
    model = AudioTrack
    template_name = 'download/audio_detail.html'
    context_object_name = 'audio'
