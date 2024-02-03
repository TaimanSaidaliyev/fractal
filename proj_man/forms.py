from django import forms
from .models import Tasks, UserSelfCategoryDictionary, TimeTracking, Project, TaskAnswerByExecutors, Status
from django.forms import formset_factory


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = (
            'title',
            'priority',
            'description',
            'parent',
            'bdate',
            'edate',
            'tdate',
            'status',
            'estimated_time',
            'is_completed',
            'executor',
            'co_executor',
            'viewers',
            'progress',
            'project',
            'author')
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'priority': forms.Select(attrs={"class": "form-select"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'parent': forms.Select(attrs={"class": "form-select", "data-control": "select2"}),
            'bdate': forms.DateInput(attrs={"class": "form-control", "id":"kt_datepicker_bdate"}),
            'edate': forms.DateInput(attrs={"class": "form-control", "id":"kt_datepicker_edate"}),
            'tdate': forms.DateInput(attrs={"class": "form-control", "id":"kt_datepicker_tdate"}),
            'status': forms.Select(attrs={"class": "form-select"}),
            'is_completed': forms.CheckboxInput(attrs={"class": "form-check-input"}),
            'author': forms.Select(attrs={"class": "form-select", "data-control": "select2", "data-placeholder": "Выберите пользователя"}),
            'executor': forms.Select(attrs={"class": "form-select", "data-control": "select2", "data-placeholder": "Выберите пользователя"}),
            'co_executor': forms.SelectMultiple(attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false", "data-placeholder": "Выберите пользователя", "data-allow-clear": "true", "multiple": "multiple"}),
            'viewers': forms.SelectMultiple(attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false", "data-placeholder": "Выберите пользователя", "data-allow-clear": "true", "multiple":"multiple"}),
            'progress': forms.NumberInput(attrs={"class": "form-range", "type": "range", "min": "0", "max": "100", "step": "10"}),
            'estimated_time': forms.NumberInput(attrs={"class": "form-control"}),
            'project': forms.Select(attrs={"class": "form-select"}),
            }


class AddUserCategory(forms.ModelForm):
    class Meta:
        model = UserSelfCategoryDictionary
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"})
        }


class AddRelatedTasks(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('related_tasks',)
        widgets = {
            'related_tasks': forms.SelectMultiple(attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false", "data-placeholder": "Выберите задачу", "data-allow-clear": "true", "multiple": "multiple"}),
        }


class AddTimeTrackingForm(forms.ModelForm):
    class Meta:
        model = TimeTracking
        fields = ('description', 'track_date', 'spent_time',)
        widgets = {
            'description': forms.TextInput(attrs={"class": "form-control"}),
            'track_date': forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            'spent_time': forms.NumberInput(attrs={"class": "form-control", "min": "1", "max": "24", "step": "1"}),
        }


AddTimeTrackingFormSet = formset_factory(AddTimeTrackingForm, extra=1)


class AnswerByAuthorForm(forms.ModelForm):
    class Meta:
        model = TaskAnswerByExecutors
        fields = ('answer_description',)
        widgets = {'answer_description': forms.Textarea(attrs={"class": "form-control"}),}


class AddProjectUsers(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('participants', )
        widgets = {
            'participants': forms.SelectMultiple(attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false", "data-placeholder": "Выберите пользователя", "data-allow-clear": "true", "multiple": "multiple"}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'bdate',
            'edate',
            'status',
            'status_tasks',
            'priority_tasks',
            'managers',
            'moderators',
            'participants',
            'category',
            'photo',
        )
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'bdate': forms.DateInput(attrs={"class": "form-control", "id": "kt_datepicker_bdate"}),
            'edate': forms.DateInput(attrs={"class": "form-control", "id": "kt_datepicker_edate"}),
            'status': forms.Select(attrs={"class": "form-select"}),
            'status_tasks': forms.SelectMultiple(
                attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false",
                       "data-placeholder": "Выберите задачу", "data-allow-clear": "true", "multiple": "multiple"}),
            'priority_tasks': forms.SelectMultiple(
                attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false",
                       "data-placeholder": "Выберите задачу", "data-allow-clear": "true", "multiple": "multiple"}),
            'managers': forms.SelectMultiple(
                attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false",
                       "data-placeholder": "Выберите задачу", "data-allow-clear": "true", "multiple": "multiple"}),
            'moderators': forms.SelectMultiple(
                attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false",
                       "data-placeholder": "Выберите задачу", "data-allow-clear": "true", "multiple": "multiple"}),
            'participants': forms.SelectMultiple(
                attrs={"class": "form-control", "data-control": "select2", "data-close-on-select": "false",
                       "data-placeholder": "Выберите задачу", "data-allow-clear": "true", "multiple": "multiple"}),
            'category': forms.Select(attrs={"class": "form-select"}),
            'photo': forms.FileInput(attrs={"class":"form-control"}),
        }