import datetime

from common.views import save_files_by_module
from proj_man.functions.taskchangefield.comparision import task_change_status
from proj_man.models import TaskApproveStatus, TaskApproveStatusActions, Tasks, TaskAnswerByExecutors, Status
from proj_man.forms import AnswerByAuthorForm
from common.forms import FileForm
from common.models import ModuleName


def is_task_executor(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    access = False
    for co_executor in task.co_executor.all():
        if (co_executor == request.user):
            access = True
    if (task.executor == request.user):
        access = True
    return access


def task_change_approve_status(request, task_id, current_status):
    task = Tasks.objects.get(pk=task_id)
    model = TaskApproveStatusActions.objects.get(task=task)
    form = AnswerByAuthorForm(request.POST)
    file_form = FileForm()
    module_id = ModuleName.objects.get(pk=3)
    if (current_status == 1 and is_task_executor(request, task_id)):
        status = TaskApproveStatus.objects.get(pk=2)
        model.approve_status = status
        model.user_sent_at = datetime.datetime.now()
        model.save()
        if form.is_valid():
            files = request.FILES.getlist('attached_file')
            save_files_by_module(request, files, module_id, model)
            try:
                answer_model = TaskAnswerByExecutors.objects.get(task=task)
            except:
                answer_model = TaskAnswerByExecutors()
            answer_model.answer_description = form.cleaned_data['answer_description']
            answer_model.task = task
            answer_model.author = request.user
            answer_model.save()
            task_change_status(request, task, 'sent_by_executor')


    elif (current_status == 2 and task.author == request.user):
        change_task = Tasks.objects.get(pk=task.pk)
        status = Status.objects.get(pk=2)
        change_task.progress = 100
        change_task.status = status
        change_task.is_completed = True
        change_task.save()
        status = TaskApproveStatus.objects.get(pk=3)
        model.approve_status = status
        model.save()
        task_change_status(request, task, 'approve_by_author')


def task_deny_approve_status(request, task_id, current_status):
    task = Tasks.objects.get(pk=task_id)
    model = TaskApproveStatusActions.objects.get(task=task)
    if (current_status == 2 and task.author == request.user):
        change_task = Tasks.objects.get(pk=task.pk)
        status = Status.objects.get(pk=5)
        change_task.progress = 100
        change_task.status = status
        change_task.is_completed = False
        change_task.save()
        status = TaskApproveStatus.objects.get(pk=1)
        model.approve_status = status
        model.save()
        task_change_status(request, task, 'deny_by_author')


def task_by_action_status(request, tasks_list, status):
    actions = TaskApproveStatusActions.objects.filter(task__in=tasks_list, approve_status=2, task__author=request.user)
    return actions