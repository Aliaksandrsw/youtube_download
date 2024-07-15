from django import forms


class YouTubeURLForm(forms.Form):
    youtube_url = forms.URLField(
        label='YouTube URL',
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.youtube.com/watch?v=...'}),
    )
