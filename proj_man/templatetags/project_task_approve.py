from django import template

from proj_man.functions.taskapprove.changeapprovetask import is_task_executor
from proj_man.models import Tasks, TaskApproveStatusActions, TaskApproveStatus, TaskAnswerByExecutors
from proj_man.forms import AnswerByAuthorForm
from common.forms import FileForm


register = template.Library()


def get_task_approved_status(task_id):
    # Создаем запись согласования в таблице если ее нет
    task = Tasks.objects.get(pk=task_id)
    try:
        status = TaskApproveStatusActions.objects.get(task=task_id)
    except:
        new_status = TaskApproveStatusActions()
        default_status = TaskApproveStatus.objects.get(id_status=0)
        new_status.task = task
        new_status.approve_status = default_status
        new_status.save()
        status = TaskApproveStatusActions.objects.get(task=task)

    return status.approve_status.pk


@register.inclusion_tag('proj_man/widgets/project_task_approve_button.html')
def show_approve_status_default(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    file_form = FileForm()
    try:
        previous_answer = TaskAnswerByExecutors.objects.get(task=task)
        form = AnswerByAuthorForm(instance=previous_answer)
    except:
        form = AnswerByAuthorForm()
    if (get_task_approved_status(task_id) == 1 and is_task_executor(request, task_id)):
        return {
            'status': get_task_approved_status(task_id),
            'form_answer': form,
            'task_id': task_id,
            'file_form': file_form,
        }


@register.inclusion_tag('proj_man/widgets/project_task_approve_button.html')
def show_approve_status_send_to_review(request, task_id):
    task = Tasks.objects.get(pk=task_id)

    if (get_task_approved_status(task_id) == 2 and task.author == request.user):
        return {
            'status': get_task_approved_status(task_id),
            'task_id': task_id,
            'author': True
        }
    if (get_task_approved_status(task_id) == 2 and is_task_executor(request, task_id)):
        return {
            'status': get_task_approved_status(task_id),
            'task_id': task_id,
            'executor': True
        }


@register.inclusion_tag('proj_man/widgets/project_task_approve_button.html')
def show_approve_status_send_to_approval(request, task_id):
    if (get_task_approved_status(task_id) == 3):
        return {
            'status': get_task_approved_status(task_id)
        }
    else:
        return None


@register.inclusion_tag('proj_man/widgets/project_task_approve_button.html')
def show_answer(request, task_id):
    if (get_task_approved_status(task_id) != 1):
        task = Tasks.objects.get(pk=task_id)
        answer = TaskAnswerByExecutors.objects.get(task=task)
        is_answer_exist = False
        if (len(answer.answer_description) > 0):
            is_answer_exist = True

        action = TaskApproveStatusActions.objects.get(task=task)
        return {
            'answer': answer,
            'type': 'answer',
            'request': request,
            'action': action,
            'is_answer_exist': is_answer_exist,
        }


