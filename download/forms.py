from django import forms


class YouTubeURLForm(forms.Form):
    youtube_url = forms.URLField(label='YouTube URL')
    download_type = forms.ChoiceField(
        choices=[('audio', 'Аудио (MP3)'), ('video', 'Видео (MP4)')],
        widget=forms.RadioSelect,
        initial='audio'
    )