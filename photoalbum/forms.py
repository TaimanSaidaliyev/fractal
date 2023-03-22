from django.contrib.auth.models import User
from django import forms
from .models import PhotoAlbume, PhotoAlbumeItem


class AddPhotoAlbume(forms.ModelForm):
    class Meta:
        model = PhotoAlbume
        fields = ('title', 'event_at', 'event_description', 'category', 'image', 'author')
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'event_at': forms.DateInput(attrs={"class":"form-control"}),
            'event_description': forms.Textarea(attrs={"class":"form-control"}),
            'author': forms.Select(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'image': forms.FileInput(attrs={"class":"form-control"}),
        }


class AddPhotoAlbumItem(forms.ModelForm):
    class Meta:
        model = PhotoAlbumeItem
        fields = ('image', )
        widgets = {
            'image': forms.FileInput(attrs={"class":"form-control", 'multiple': True}),
        }
