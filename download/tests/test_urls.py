from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views


class UrlsTest(SimpleTestCase):
    def test_download_youtube_url_resolves(self):
        url = reverse('download_youtube')
        self.assertEqual(resolve(url).func.view_class, views.DownloadYouTubeView)

    def test_audio_detail_url_resolves(self):
        url = reverse('audio_detail', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, views.AudioDetailView)

    def test_video_detail_url_resolves(self):
        url = reverse('video_detail', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, views.VideoDetailView)

    def test_download_youtube_url_returns_correct_path(self):
        path = reverse('download_youtube')
        self.assertEqual(path, '/')

    def test_audio_detail_url_returns_correct_path(self):
        path = reverse('audio_detail', args=['test-audio'])
        self.assertEqual(path, '/audio/test-audio/')

    def test_video_detail_url_returns_correct_path(self):
        path = reverse('video_detail', args=['test-video'])
        self.assertEqual(path, '/video/test-video/')
