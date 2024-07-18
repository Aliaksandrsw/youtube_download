from django.urls import path
from . import views

urlpatterns = [
    path('', views.DownloadYouTubeView.as_view(), name='download_youtube'),
    path('audio/<slug:slug>/', views.AudioDetailView.as_view(), name='audio_detail'),
    path('video/<slug:slug>/', views.VideoDetailView.as_view(), name='video_detail'),
]