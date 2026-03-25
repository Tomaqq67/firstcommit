from django import forms
from .models import Genre, Track

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
        labels = {
            'runame':'Название на русском',
            'name':'Название',
            'description':'Описание',
        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = '__all__'
        labels = {
            'name' : 'Название',
            'duration' : 'Длительность',
            'genres' : 'Описание',
        }
