from django import forms
from .models import CommonFiles, Comments


class FileForm(forms.ModelForm):
    class Meta:
        model = CommonFiles
        fields = ('attached_file', )
        widgets = {
            'attached_file': forms.FileInput(attrs={"class":"form-control", 'multiple': True}),
}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('description', )
        widgets = {
            'description': forms.Textarea(attrs={'rows':1, 'class':"form-control form-control-solid border ps-5", 'placeholder':"Оставить комментарий"}),
        }

