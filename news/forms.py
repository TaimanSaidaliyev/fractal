from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import Textarea
from .models import Category, NewsLikes, NewsSave
from .models import News, Comments
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Ваш логин должен содержать не более 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', help_text='Ваш логин должен содержать не более 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', help_text='Пароль должен содержать минимум 8 символов с цифрами, символами и буквам', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', help_text='Пароль должен содержать минимум 8 символов с цифрами, символами и буквам', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category', 'photo', 'author']
        content = forms.CharField(widget=CKEditorUploadingWidget())
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'content': forms.Textarea(attrs={"class":"form-control"}),
            'is_published': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'category': forms.Select(attrs={"class":"form-control"}),
            'author': forms.Select(attrs={"class":"form-control"}),
        }


    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title


class CommentNews(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content', )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = ''
        self.fields['content'].widget = Textarea(attrs={'rows':1, 'class':"form-control form-control-solid border ps-5", 'placeholder':"Написать комментарий. Для отправки нажмите Ctr+Enter"})


class NewsLikesForm(forms.ModelForm):
    class Meta:
        like = NewsLikes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NewsSaveForm(forms.ModelForm):
    class Meta:
        save = NewsSave
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)