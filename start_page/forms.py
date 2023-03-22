from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-control-solid'}))


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
