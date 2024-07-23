from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.text import slugify
from ..models import AudioTrack, VideoLoad


class AudioTrackModelTest(TestCase):
    def setUp(self):
        self.audio_file = SimpleUploadedFile("test_audio.mp3", b"file_content", content_type="audio/mpeg")
        self.audio_track = AudioTrack.objects.create(
            title="Test Audio",
            audio_file=self.audio_file,
            youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )

    def test_audio_track_creation(self):
        self.assertTrue(isinstance(self.audio_track, AudioTrack))
        self.assertEqual(self.audio_track.__str__(), self.audio_track.title)

    def test_audio_track_slug(self):
        self.assertEqual(self.audio_track.slug, slugify(self.audio_track.title))

    def test_audio_track_file_upload(self):
        self.assertTrue(self.audio_track.audio_file.name.startswith('audio_tracks/'))


class VideoLoadModelTest(TestCase):
    def setUp(self):
        self.video_file = SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4")
        self.video_load = VideoLoad.objects.create(
            title="Test Video",
            video_file=self.video_file,
            youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )

    def test_video_load_creation(self):
        self.assertTrue(isinstance(self.video_load, VideoLoad))
        self.assertEqual(self.video_load.__str__(), self.video_load.title)

    def test_video_load_slug(self):
        self.assertEqual(self.video_load.slug, slugify(self.video_load.title))

    def test_video_load_file_upload(self):
        self.assertTrue(self.video_load.video_file.name.startswith('video/'))
