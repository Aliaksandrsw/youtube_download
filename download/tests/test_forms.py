from django.test import TestCase
from download.forms import YouTubeURLForm
from django import forms


class YouTubeURLFormTest(TestCase):
    def test_form_fields(self):
        form = YouTubeURLForm()
        self.assertTrue('youtube_url' in form.fields)
        self.assertTrue('download_type' in form.fields)

    def test_youtube_url_field(self):
        form = YouTubeURLForm()
        self.assertIsInstance(form.fields['youtube_url'], forms.URLField)

    def test_download_type_field(self):
        form = YouTubeURLForm()
        self.assertIsInstance(form.fields['download_type'], forms.ChoiceField)
        self.assertEqual(form.fields['download_type'].widget.__class__, forms.RadioSelect)
        self.assertEqual(form.fields['download_type'].initial, 'audio')

    def test_valid_data(self):
        form_data = {
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'download_type': 'audio'
        }
        form = YouTubeURLForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_url(self):
        form_data = {
            'youtube_url': 'not-a-url',
            'download_type': 'audio'
        }
        form = YouTubeURLForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('youtube_url' in form.errors)

    def test_invalid_download_type(self):
        form_data = {
            'youtube_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'download_type': 'invalid_type'
        }
        form = YouTubeURLForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('download_type' in form.errors)
