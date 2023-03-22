import json

from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from .functions.taskapprove.changeapprovetask import task_change_approve_status, task_deny_approve_status, task_by_action_status
from .models import Tasks, Project, UserSelfCategory, UserSelfCategoryDictionary, UserSelfSavedTasks, TimeTracking, TaskApproveStatusActions, Status, Priority
from .forms import TaskForm, AddRelatedTasks, AddTimeTrackingForm, ProjectForm, AddProjectUsers, AddTimeTrackingFormSet
from django.db.models import Count
from django.urls import reverse
from django.db.models import Q
from common.models import ModuleName
from common.forms import FileForm
from common.views import save_files_by_module, delete_common_files_by_record, delete_common_comments_by_record
from .functions.taskchangefield.comparision import task_change_fields_comparison
from django.contrib.auth.models import User


def view_tasks(request, project_id):
    template = 'proj_man/project_tasks_list.html'
    tasks_list = Tasks.objects.filter(project=project_id)
    page_type = 'my_projects'
    project = Project.objects.get(pk=project_id)
    context = {
        'tasks_list': tasks_list,
        'project': project,
        'page_type': page_type,
        'actions': task_by_action_status(request, tasks_list, 2),
    }
    return render(request, template, context)


def view_task_detail(request, task_id):
    template = 'proj_man/project_tasks_detail.html'
    page_type = 'my_projects'
    task = Tasks.objects.get(pk=task_id)
    project_id = task.project.pk
    project = Project.objects.get(pk=project_id)
    users = project.participants.all()
    module_id = 1
    can_delete = False
    saved = False
    try:
        saved = UserSelfSavedTasks.objects.get(user=request.user, task=task)
    except:
        None

    if(saved):
        saved = True

    if(task.author==request.user):
        can_delete = True

    is_current_user_access = False
    for user in users:
        if (user == request.user):
            is_current_user_access = True
    if (is_current_user_access == False):
        return redirect('error_404')

    context = {
        'task': task,
        'page_type': page_type,
        'saved': saved,
        'can_delete': can_delete,
        'module_id': module_id,
    }
    return render(request, template, context)


def update_task(request, task_id):
    model = Tasks.objects.get(pk=task_id)
    task = Tasks.objects.get(pk=task_id)
    form = TaskForm(instance=model)
    form_type = 'update'
    template = 'proj_man/project_tasks_add.html'
    project = Project.objects.get(pk=model.project.pk)
    add_task_by_project_filter_fields(request, project, form)
    file_form = FileForm()
    module_id = ModuleName.objects.get(pk=1)
    if request.method == 'POST':
        files = request.FILES.getlist('attached_file')
        form = TaskForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            model.object = form.save()
            project = Project.objects.get(pk=project.pk)
            model.object.project = project
            model.object.save()
            task_change_fields_comparison(request, form, task)
            record_id = Tasks.objects.get(pk=model.object.pk)
            save_files_by_module(request, files, module_id, record_id)
            return redirect(reverse('projects_task_detail', kwargs={'task_id': task_id}))
    context = {
        'form': form,
        'form_type': form_type,
        'project': project,
        'task': model,
        'file_form': file_form,
    }

    return render(request, template, context)


def add_task(request):
    template = 'proj_man/project_tasks_add.html'
    model = Tasks
    form_type = 'add_task'
    form = TaskForm(request.POST)
    file_form = FileForm()
    module_id = ModuleName.objects.get(pk=1)
    if request.method == 'POST':
        files = request.FILES.getlist('attached_file')
        if form.is_valid():
            model.object = form.save()
            model.object.save()
            record_id = Tasks.objects.get(pk=model.object.pk)
            save_files_by_module(request, files, module_id, record_id)
            return redirect(reverse('projects_task_detail', kwargs={'task_id': model.object.pk}))

    context = {
        'form_type': form_type,
        'form': form,
        'file_form': file_form,
    }

    return render(request, template, context)


def add_task_by_project_filter_fields(request, project, form):
    form.fields['parent'].queryset = Tasks.objects.filter(project=project.pk)
    form.fields['status'].queryset = Status.objects.filter(status_tasks=project.pk)
    form.fields['priority'].queryset = Priority.objects.filter(priority_tasks=project.pk)
    form.fields['author'].queryset = User.objects.filter(
        Q(pk__in=project.participants.all()) | Q(pk__in=project.moderators.all()) | Q(pk__in=project.managers.all()))
    form.fields['executor'].queryset = User.objects.filter(
        Q(pk__in=project.participants.all()) | Q(pk__in=project.moderators.all()) | Q(pk__in=project.managers.all()))
    form.fields['co_executor'].queryset = User.objects.filter(
        Q(pk__in=project.participants.all()) | Q(pk__in=project.moderators.all()) | Q(pk__in=project.managers.all()))
    form.fields['viewers'].queryset = User.objects.filter(
        Q(pk__in=project.participants.all()) | Q(pk__in=project.moderators.all()) | Q(pk__in=project.managers.all()))
    return form


def add_project_task(request, project_id):
    template = 'proj_man/project_tasks_add.html'
    form_type = 'add'
    model = Tasks
    project = Project.objects.get(pk=project_id)
    form = TaskForm(initial={'project': project})
    add_task_by_project_filter_fields(request, project, form)
    file_form = FileForm()
    module_id = ModuleName.objects.get(pk=1)
    if request.method == 'POST':
        files = request.FILES.getlist('attached_file')
        form = TaskForm(request.POST)
        if form.is_valid():
            model.object = form.save()
            model.object.project = project
            model.object.save()
            record_id = Tasks.objects.get(pk=model.object.pk)
            save_files_by_module(request, files, module_id, record_id)
            return redirect(reverse('projects_task_detail', kwargs={'task_id': record_id.pk}))

    context = {
        'form_type': form_type,
        'form': form,
        'project': project,
        'file_form': file_form,
    }
    return render(request, template, context)


def add_project_sub_task(request, project_id, task_id):
    template = 'proj_man/project_tasks_add.html'
    form_type = 'add_sub_task'
    model = Tasks
    project = Project.objects.get(pk=project_id)
    parent = Tasks.objects.get(pk=task_id)
    form = TaskForm(initial={'project': project, 'parent': parent})
    add_task_by_project_filter_fields(request, project, form)
    file_form = FileForm()
    module_id = ModuleName.objects.get(pk=1)
    if request.method == 'POST':
        files = request.FILES.getlist('attached_file')
        form = TaskForm(request.POST)
        if form.is_valid():
            model.object = form.save()
            model.object.project = project
            model.object.parent = parent
            model.object.save()
            record_id = Tasks.objects.get(pk=model.object.pk)
            save_files_by_module(request, files, module_id, record_id)
            return redirect(reverse('projects_task_detail', kwargs={'task_id': record_id.pk}))

    context = {
        'form_type': form_type,
        'form': form,
        'project': project,
        'file_form': file_form,
        'task': parent,
    }
    return render(request, template, context)


def delete_task(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    module = ModuleName.objects.get(pk=1)
    if (task.author==request.user):
        delete_common_files_by_record(task_id, module_id=1)
        delete_common_comments_by_record(task_id, module.pk)
        task.delete()
    else:
        return redirect('error_404')
    return redirect('project_main')


def add_related_tasks(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    form = AddRelatedTasks(instance=task)
    if (request.method == 'POST'):
        form = AddRelatedTasks(request.POST, instance=task)
        if form.is_valid():
            task.related_tasks.set(form.cleaned_data['related_tasks'])
            task.save()
            return redirect(reverse('projects_task_detail', kwargs={'task_id': task_id}))


def view_project_list(request):
    template = 'proj_man/projects_list.html'
    tasks = Tasks.objects.annotate(cnt=Count('project'))
    page_type = 'my_projects'
    context = {
        'tasks': tasks,
        'page_type': page_type,
    }
    return render(request, template, context)


def view_project_my_tasks(request):
    template = 'proj_man/project_main_page.html'
    tasks_list = Tasks.objects.filter(Q(executor=request.user.pk) | Q(co_executor=request.user.pk), status=1).distinct()
    page_type = 'my_tasks'
    context = {
        'tasks_list': tasks_list,
        'executor': request.user.pk,
        'page_type': page_type,
    }
    return render(request, template, context)


def view_project_tasks_by_self_user(request):
    template = 'proj_man/project_main_page.html'
    tasks_list = Tasks.objects.filter(author=request.user).distinct()
    count = tasks_list.count()
    page_type = 'self_user_tasks'
    context = {
        'tasks_list': tasks_list,
        'executor': request.user.pk,
        'page_type': page_type,
        'count': count,
    }
    return render(request, template, context)


def view_project_tasks_by_user_self_category(request, category_id):
    template = 'proj_man/project_main_page.html'
    tasks_list = Tasks.objects.filter(user_self_category_task__category=category_id)
    category = UserSelfCategoryDictionary.objects.get(pk=category_id)
    page_type = 'user_self_category'
    context = {
        'tasks_list': tasks_list,
        'executor': request.user.pk,
        'category_id': category_id,
        'category': category,
        'page_type': page_type,
    }
    return render(request, template, context)


def view_project_saved_tasks_by_user_self(request):
    template = 'proj_man/project_main_page.html'
    tasks_list = Tasks.objects.filter(user_self_saved_task__user=request.user.pk)
    page_type = 'user_self_saved_tasks'
    context = {
        'tasks_list': tasks_list,
        'executor': request.user.pk,
        'page_type': page_type,
    }
    return render(request, template, context)


def view_project_viewers_task(request):
    template = 'proj_man/project_main_page.html'
    tasks_list = Tasks.objects.filter(viewers=request.user.pk)
    page_type = 'user_viewers_task_list'
    context = {
        'tasks_list': tasks_list,
        'executor': request.user.pk,
        'page_type': page_type,
    }
    return render(request, template, context)


def add_user_category(request):
    model = UserSelfCategoryDictionary()
    category_title = request.POST.get('title')
    previous_page = request.POST.get('next', '/')
    user = request.user
    if request.method == 'POST':
        model.title = category_title
        model.user = user
        model.save()
        return HttpResponseRedirect(previous_page)


def rename_user_category(request, category_id):
    model = UserSelfCategoryDictionary.objects.get(pk=category_id)
    category_title = request.POST.get('title')
    previous_page = request.POST.get('next', '/')
    user = request.user
    if request.method == 'POST':
        model.title = category_title
        model.user = user
        model.save()
        return HttpResponseRedirect(previous_page)


def delete_user_category(request, category_id):
    user_category = UserSelfCategoryDictionary.objects.get(pk=category_id)
    if (user_category.user == request.user):
        user_category.delete()
        return redirect('project_main')
    else:
        return redirect('error_404')


def add_task_to_user_category(request, task_id, category_id):
    model = UserSelfCategory()
    if request.method == 'POST':
        model.task = task_id
        model.category = category_id
        context = {
            'task_id': task_id,
            'category_id': category_id
        }

        return render(request, 'proj_man/project_cher.html', context)


def save_task_user_self(request, task_id):
    model = UserSelfSavedTasks()
    task = Tasks.objects.get(pk=task_id)
    is_exist = None
    try:
        is_exist = UserSelfSavedTasks.objects.get(user=request.user, task=task)
    except:
        None

    if (is_exist):
        is_exist.delete()
    else:
        model.task = task
        model.user = request.user
        model.save()
    return redirect(reverse('projects_task_detail', kwargs={'task_id': task_id}))


def view_project_completed_tasks(request):
    template = 'proj_man/project_main_page.html'
    tasks_list = Tasks.objects.filter(Q(executor=request.user.pk) | Q(co_executor=request.user.pk), is_completed=True).distinct()
    page_type = 'completed_tasks'
    context = {
        'tasks_list': tasks_list,
        'executor': request.user.pk,
        'page_type': page_type,
    }
    return render(request, template, context)


def copy_project_task(request, project_id, task_id):
    template = 'proj_man/project_tasks_add.html'
    task = Tasks.objects.get(pk=task_id)
    model = Tasks
    form_type = 'copy_task'
    form = TaskForm(instance=task)
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        if form.is_valid():
            model.object = form.save()
            project = Project.objects.get(pk=project_id)
            model.object.project = project
            model.object.save()
            return redirect(reverse('projects_task_detail', kwargs={'task_id': model.object.pk}))

    context = {
        'form_type': form_type,
        'form': form,
        'project': project,
        'task': task
    }

    return render(request, template, context)


def add_time_tracking_by_task(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    form = AddTimeTrackingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            model = TimeTracking()
            model.description = form.cleaned_data['description']
            model.task = task
            model.spent_time = form.cleaned_data['spent_time']
            model.track_date = form.cleaned_data['track_date']
            model.author = request.user
            model.save()
    context = {
        'form': form,
        'task': task,
    }
    return redirect(reverse('projects_task_detail', kwargs={'task_id': task.pk}))


def delete_time_tracking(request, time_tracking_id):
    time_tracking = TimeTracking.objects.get(pk=time_tracking_id)
    task = time_tracking.task
    time_tracking.delete()
    return redirect(reverse('projects_task_detail', kwargs={'task_id': task.pk}))


def task_change_approve_status_view(request, task_id, current_status):
    task_change_approve_status(request, task_id, current_status)
    return redirect(reverse('projects_task_detail', kwargs={'task_id': task_id}))


def task_deny_approve_status_view(request, task_id, current_status):
    task_deny_approve_status(request, task_id, current_status)
    return redirect(reverse('projects_task_detail', kwargs={'task_id': task_id}))


def add_project(request):
    templates = 'proj_man/project_add.html'
    page_type = 'add_project'
    form = ProjectForm(request.POST, request.FILES)
    model = Project
    context = {
        'form': form,
        'page_type': page_type,
    }
    if (request.method == 'POST'):
        model.object = form.save()
        model.object.save()
        return redirect(reverse('projects_tasks_list', kwargs={'project_id': model.object.pk}))

    return render(request, templates, context)


def update_project(request, project_id):
    templates = 'proj_man/project_add.html'
    model = Project.objects.get(pk=project_id)
    form = ProjectForm(instance=model)
    page_type = 'update_project'
    if (request.method == 'POST'):
        form = ProjectForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            model.object = form.save()
            model.object.save()
            return redirect(reverse('projects_tasks_list', kwargs={'project_id': project_id}))
    context = {
        'form': form,
        'project_id': project_id,
        'page_type': page_type,
        'project': model,
    }
    return render(request, templates, context)


def delete_project(request, project_id):
    if (request.method == "POST"):
        model = Project.objects.get(pk=project_id)
        status = Status.objects.get(title_tech='deleted')
        model.status = status
        model.save()
        return redirect(reverse('projects_list'))
    else:
        return redirect(reverse('error_404'))


def delete_project_completely(request, project_id):
    if (request.method == "POST"):
        model = Project.objects.get(pk=project_id)
        model.delete()
        return redirect(reverse('projects_list'))
    else:
        return redirect(reverse('error_404'))


def allow_to_project(request):
    projects = Project.objects.exclude(status__title_tech='deleted').filter(participants=request.user).filter(managers=request.user).filter(moderators=request.user)


def add_project_users(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = AddProjectUsers(instance=project)
    if (request.method == 'POST'):
        form = AddProjectUsers(request.POST, instance=project)
        if form.is_valid():
            project.participants.set(form.cleaned_data['participants'])
            project.save()
            return redirect(reverse('projects_tasks_list', kwargs={'project_id': project.pk}))


def add_time_tracking_by_task_multi(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    template = 'todo/todo_cher.html'
    formset = AddTimeTrackingFormSet(request.POST)
    if (request.method == 'POST'):
        formset = AddTimeTrackingFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                track_date = form.cleaned_data.get('track_date')
                description = form.cleaned_data.get('description')
                spent_time = form.cleaned_data.get('spent_time')
                TimeTracking(track_date=track_date, description=description, spent_time=spent_time).save()
            return redirect(reverse('add_time_tracking_by_task_multi'))

    context = {
        'formset': formset
    }

    return render(request, template, context)