from proj_man.models import TaskChangeHistory, TaskChangeHistoryAction


def task_change_status(request, task, activity):
    model_history_action = TaskChangeHistoryAction()
    model_history_action.task = task
    model_history_action.user = request.user
    model_history_action.save()
    model_history = TaskChangeHistory()
    model_history.task_change_action = model_history_action
    model_history.column = activity
    model_history.save()



def task_change_fields_comparison(request, form, task):
    model_history_action = TaskChangeHistoryAction()
    model_history_action.task = task
    model_history_action.user = request.user
    model_history_action.save()
    change_count = 0

    if (form.cleaned_data['title'] != task.title):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'title'
        model_history.first_value = task.title
        model_history.finish_value = form.cleaned_data['title']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['description'] != task.description):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'description'
        model_history.first_value = task.description
        model_history.finish_value = form.cleaned_data['description']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['parent'] != task.parent):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'parent'
        model_history.first_value = task.parent
        model_history.finish_value = form.cleaned_data['parent']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['priority'] != task.priority):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'priority'
        model_history.first_value = task.priority
        model_history.finish_value = form.cleaned_data['priority']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['status'] != task.status):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'status'
        model_history.first_value = task.status
        model_history.finish_value = form.cleaned_data['status']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['progress'] != task.progress):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'progress'
        model_history.first_value = task.progress
        model_history.finish_value = form.cleaned_data['progress']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['is_completed'] != task.is_completed):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'is_completed'
        model_history.first_value = task.is_completed
        model_history.finish_value = form.cleaned_data['is_completed']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['bdate'] != task.bdate):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'bdate'
        model_history.first_value = task.bdate
        model_history.finish_value = form.cleaned_data['bdate']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['edate'] != task.edate):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'edate'
        model_history.first_value = task.edate
        model_history.finish_value = form.cleaned_data['edate']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['tdate'] != task.tdate):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'tdate'
        model_history.first_value = task.tdate
        model_history.finish_value = form.cleaned_data['tdate']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['estimated_time'] != task.estimated_time):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'estimated_time'
        model_history.first_value = task.estimated_time
        model_history.finish_value = form.cleaned_data['estimated_time']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['author'] != task.author):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'author'
        model_history.first_value = task.author
        model_history.finish_value = form.cleaned_data['author']
        model_history.save()
        change_count = change_count + 1

    if (form.cleaned_data['executor'] != task.executor):
        model_history = TaskChangeHistory()
        model_history.task_change_action = model_history_action
        model_history.column = 'executor'
        model_history.first_value = task.executor
        model_history.finish_value = form.cleaned_data['executor']
        model_history.save()
        change_count = change_count + 1

    if change_count == 0:
        model_history_action.delete()