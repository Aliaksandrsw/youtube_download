from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import AudioTrack, VideoLoad
from unittest.mock import patch, MagicMock


class DownloadYouTubeViewTest(TestCase):
    def setUp(self):
        self.url = reverse('download_youtube')

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'download/index.html')

    @patch('download.views.download_audio')
    def test_post_request_audio(self, mock_download_audio):
        mock_audio = MagicMock(spec=AudioTrack)
        mock_audio.slug = 'test-audio'
        mock_download_audio.return_value = mock_audio

        data = {
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'download_type': 'audio'
        }
        response = self.client.post(self.url, data)

        self.assertRedirects(
            response,
            reverse('audio_detail', kwargs={'slug': 'test-audio'}),
            fetch_redirect_response=False
        )

        mock_download_audio.assert_called_once_with('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


class AudioDetailViewTest(TestCase):
    def setUp(self):
        self.audio = AudioTrack.objects.create(
            title='Test Audio',
            audio_file=SimpleUploadedFile("test_audio.mp3", b"file_content", content_type="audio/mpeg"),
            youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        )
        self.url = reverse('audio_detail', kwargs={'slug': self.audio.slug})

    def test_audio_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'download/audio_detail.html')
        self.assertEqual(response.context['audio'], self.audio)


class VideoDetailViewTest(TestCase):
    def setUp(self):
        self.video = VideoLoad.objects.create(
            title='Test Video',
            video_file=SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4"),
            youtube_url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        )
        self.url = reverse('video_detail', kwargs={'slug': self.video.slug})

    def test_video_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'download/video_detail.html')
        self.assertEqual(response.context['video'], self.video)
