from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={"class":"form-control"}),
            'last_name': forms.TextInput(attrs={"class":"form-control"}),
            'email': forms.EmailInput(attrs={"class":"form-control"}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fathers_name', 'person_id', 'bio', 'location', 'birth_date', 'start_date', 'education',
                  'telephone', 'telephone_job', 'skype', 'instagram', 'linkedin', 'facebook', 'certificate', 'honor', 'bio', 'website', 'quote',
                  'company', 'department', 'gender', 'job_title', 'status', 'photo')
        widgets = {
            'fathers_name': forms.TextInput(attrs={"class":"form-control"}),
            'person_id': forms.TextInput(attrs={"class":"form-control"}),
            'birth_date': forms.DateInput(attrs={"class":"form-control"}),
            'start_date': forms.SelectDateWidget(attrs={"class":"form-control"}),
            'education': forms.TextInput(attrs={"class":"form-control"}),
            'location': forms.TextInput(attrs={"class":"form-control"}),
            'telephone': forms.TextInput(attrs={"class":"form-control"}),
            'telephone_job': forms.TextInput(attrs={"class":"form-control"}),
            'skype': forms.TextInput(attrs={"class":"form-control"}),
            'instagram': forms.TextInput(attrs={"class":"form-control"}),
            'linkedin': forms.TextInput(attrs={"class":"form-control"}),
            'facebook': forms.TextInput(attrs={"class":"form-control"}),
            'certificate': forms.SelectMultiple(attrs={"class":"form-control"}),
            'honor': forms.SelectMultiple(attrs={"class":"form-control"}),
            'bio': forms.Textarea(attrs={"class":"form-control"}),
            'website': forms.TextInput(attrs={"class":"form-control"}),
            'quote': forms.Textarea(attrs={"class":"form-control"}),
            'company': forms.Select(attrs={"class":"select-selection select-selection--single form-select"}),
            'department': forms.Select(attrs={"class":"select-selection select-selection--single form-select"}),
            'gender': forms.Select(attrs={"class":"select-selection select-selection--single form-select"}),
            'job_title': forms.Select(attrs={"class":"select-selection select-selection--single form-select"}),
            'status': forms.Select(attrs={"class":"select-selection select-selection--single form-select"}),
        }
