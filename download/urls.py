from django.urls import path
from . import views

urlpatterns = [
    path('', views.DownloadYouTubeAudioView.as_view(), name='download_youtube_audio'),
    path('audio/<slug:slug>/', views.AudioDetailView.as_view(), name='audio_detail'),
]