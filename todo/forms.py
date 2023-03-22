from django import forms
from .models import ToDo, PriorityToDo, Files
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'priority', 'description', 'bdate', 'edate', 'completed', 'reminder', 'progress', 'status', 'author', 'executor')
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),
            'priority': forms.Select(attrs={"class":"form-control"}),
            'bdate': forms.DateInput(attrs={"class":"form-control form-control-solid ps-12", "type":"text", "placeholder":"Select a date"}),
            'edate': forms.DateInput(attrs={"class":"form-control form-control-solid ps-12", "type":"text", "placeholder":"Select a date"}),
            'completed': forms.CheckboxInput(attrs={"class":"form-check-input", "for":"flexSwitchCheckDefault"}),
            'reminder': forms.CheckboxInput(attrs={"class":"form-check-input"}),
            'progress': forms.NumberInput(attrs={"class":"form-control", "step":"10", "min":"0", "max":"100"}),
            'status': forms.Select(attrs={"class":"form-control"}),
            'author': forms.Select(attrs={"class":"form-control"}),
            'executor': forms.Select(attrs={"class":"form-control"}),
}


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('attached_file', )
        widgets = {
            'attached_file': forms.FileInput(attrs={"class":"form-control", 'multiple': True}),
}
