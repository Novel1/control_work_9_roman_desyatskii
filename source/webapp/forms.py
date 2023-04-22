from django import forms

from webapp.models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:

        model = Photo
        fields = ('title', 'avatar')
        labels = {
            'title': 'Подпись',
            'avatar': 'Фото',
        }


class FavoriteForm(forms.Form):
    note = forms.CharField(max_length=30, required=True, label='Заметка')
