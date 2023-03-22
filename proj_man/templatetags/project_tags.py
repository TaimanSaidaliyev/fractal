from django import template

from proj_man.forms import AddTimeTrackingForm, AddProjectUsers, AddRelatedTasks
from proj_man.models import Project, Tasks, UserSelfCategoryDictionary, TimeTracking
from django.db.models import *
from django.contrib.auth.models import User
from profile_add.models import Profile

register = template.Library()


@register.inclusion_tag('proj_man/widgets/project_description_header.html')
def show_project_description(project_id):
    project = Project.objects.get(pk=project_id)
    form_project_user = AddProjectUsers(instance=project)
    context = {
        'project': project,
        'form_project_user': form_project_user,
    }
    return context


@register.filter()
def upfirstletter(value):
    first = value[0] if len(value) > 0 else ''
    return first.upper()


@register.filter()
def exludefirstletter(value):
    first = value[1:] if len(value) > 0 else ''
    return first


@register.inclusion_tag('proj_man/widgets/progress_bar_list.html')
def show_task_progress(task_id):
    task_progress = Tasks.objects.get(pk=task_id)
    percent = task_progress.progress
    color = 2
    if (percent < 25):
        color = 'bg-danger'
    elif (percent >= 25 and percent < 75):
        color = 'bg-warning'
    else:
        color = 'bg-success'
    context = {
        'color': color,
        'percent': percent,
        'task_progress': task_progress,
    }
    return context


@register.inclusion_tag('proj_man/widgets/project_task_history.html')
def show_task_history(task_id):
    task_progress = Tasks.objects.get(pk=task_id)
    context = {
        'task_progress': task_progress
    }
    return context


@register.inclusion_tag('proj_man/widgets/project_sidebar.html')
def show_proj_man_sidebar(request, page_type, category_id):
    user_self_categories = UserSelfCategoryDictionary.objects.annotate(cnt=Count('user_self_category')).filter(user=request.user.pk)
    count_my_task = Tasks.objects.filter(Q(executor=request.user.pk) | Q(co_executor=request.user.pk), status=1).distinct().count
    count_saved_tasks = Tasks.objects.filter(user_self_saved_task__user=request.user.pk).count
    count_my_projects = Project.objects.filter(participants=request.user.pk).count
    count_completed_tasks = Tasks.objects.filter(Q(executor=request.user.pk) | Q(co_executor=request.user.pk), is_completed=True).distinct().count
    count_user_self_tasks = Tasks.objects.filter(author=request.user).distinct().count
    context = {
        'request': request,
        'user_self_categories': user_self_categories,
        'page_type': page_type,
        'category_id': category_id,
        'count_my_task': count_my_task,
        'count_saved_tasks': count_saved_tasks,
        'count_my_projects': count_my_projects,
        'count_completed_tasks': count_completed_tasks,
        'count_user_self_tasks': count_user_self_tasks,
    }
    return context


@register.inclusion_tag('proj_man/widgets/project_task_hierarchy.html')
def show_task_hierarchy(task_id):
    task = Tasks.objects.get(pk=task_id)
    task_in_array = Tasks
    parent = task.parent
    task_hierarchy = []
    task_hierarchy.append(task)
    while ((parent is None) == False):
        task = Tasks.objects.get(pk=parent.pk)
        task_hierarchy.append(task)
        parent = task.parent
    task_hierarchy.reverse()
    tasks_count = len(task_hierarchy)
    context = {
        'task': task,
        'task_hierarchy': task_hierarchy,
        'tasks_count': tasks_count,
    }
    return context


@register.inclusion_tag('proj_man/widgets/project_task_time_tracking_add_form.html')
def show_add_time_tracking_by_task(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    form = AddTimeTrackingForm(request.POST)
    context = {
        'form': form,
        'task': task,
    }

    return context


@register.inclusion_tag('proj_man/widgets/project_task_time_tracking.html')
def show_time_tracking_by_task(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    time_tracking = TimeTracking.objects.filter(task=task)
    summ = time_tracking.aggregate(Sum('spent_time'))
    context = {
        'time_tracking': time_tracking,
        'summ': summ,
        'task': task,
    }
    return context


@register.inclusion_tag('proj_man/widgets/project_card_on_page.html')
def show_projects_cards(request, project_status):
    access = False
    profile = Profile.objects.get(user=request.user.pk)
    if (project_status == 1):
        projects = Project.objects.exclude(status__title_tech='deleted').filter(
            Q(participants=request.user) | Q(managers=request.user)).filter(company=profile.company).distinct()
    elif (project_status == 0):
        projects = Project.objects.filter(status__title_tech='deleted').filter(company=profile.company)
    context = {
        'projects': projects
    }
    return context


@register.inclusion_tag('proj_man/widgets/project_tasks_related_tasks.html')
def show_related_tasks(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    tasks_related = Tasks.objects.filter(related_tasks=task_id).distinct()
    form_related_tasks = AddRelatedTasks(instance=task)
    related_tasks_count = tasks_related.count() + task.related_tasks.count()
    context = {
        'task': task,
        'tasks_related': tasks_related,
        'form_related_tasks': form_related_tasks,
        'related_tasks_count': related_tasks_count,
    }
    return context


@register.inclusion_tag('proj_man/widgets/project_tasks_table.html')
def show_tasks_table(request, tasks_list):
    context = {
        'tasks_list': tasks_list
    }
    return context
