from .models import UserTemplate
from django.forms import Textarea
from django import forms


class InterfaceUpdateForm(forms.ModelForm):
    class Meta:
        model = UserTemplate
        fields = ['title', 'template_type', 'sidebar', 'header', 'content_type', 'is_sidebar', 'photo', 'logo_light', 'logo_dark', 'background_theme']
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'template_type': forms.Select(attrs={"class":"form-control"}),
            'sidebar': forms.Select(attrs={"class": "form-control"}),
            'is_sidebar': forms.Select(attrs={"class":"form-control"}),
            'header': forms.Select(attrs={"class":"form-control"}),
            'content_type': forms.Select(attrs={"class":"form-control"}),
        }