from django import template
from proj_man.models import Project, TaskChangeHistory, Tasks, TaskChangeHistoryAction


register = template.Library()


@register.inclusion_tag('proj_man/widgets/project_task_history.html')
def show_task_history(task_id):
    task = Tasks.objects.get(pk=task_id)
    action = TaskChangeHistoryAction.objects.filter(task_id=task.pk)
    row = TaskChangeHistory.objects.filter(task_change_action__in=action)
    context = {
        'task': task,
        'history': row,
        'action': action,
    }

    return context

