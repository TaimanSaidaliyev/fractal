from django.shortcuts import render, redirect
from .models import FileIcon, CommonFiles, Comments, ModuleName
from django.urls import reverse
from .forms import CommentForm
from proj_man.models import TaskApproveStatusActions
import os
import pathlib


def save_files_by_module(request, files, module_id, record_id):
    for file in files:
        file_name = os.path.basename("media/" + str(file))
        file_extension = pathlib.Path(file_name).suffix
        try:
            icon_id = FileIcon.objects.filter(suffix=file_extension).first()
            new_files = CommonFiles(
                id_record=record_id.pk,
                module_name=module_id,
                attached_file=file,
                icon_id=icon_id.pk,
                user_id=request.user.pk,
            )
        except:
            new_files = CommonFiles(
                id_record=record_id.pk,
                module_name=module_id,
                attached_file=file,
                icon_id=1,
                user_id=request.user.pk,
            )
        new_files.save()


def delete_common_file(request, file_id, record_id):
    file = CommonFiles.objects.get(pk=file_id)
    module = file.module_name.pk
    try:
        os.remove("media/" + str(file.attached_file))
    except:
        None
    file.delete()
    return redirect_by_module_record_id(request, record_id, module)


def delete_common_files_by_record(record_id, module_id):
    files = CommonFiles.objects.filter(id_record=record_id, module_name=module_id)
    for file in files:
        file_name = os.remove("media/" + str(file.image))
    files.delete()
    return None


def add_common_comment(request, record_id, module_id):
    module = ModuleName.objects.get(pk=module_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author=request.user,
                id_record=record_id,
                description=form.cleaned_data['description'],
                module_name=module,
                status=True,
            )
            comment.save()
            return redirect_by_module_record_id(request, record_id, module_id)


def reply_common_comment(request, record_id, module_id, comment_id):
    module = ModuleName.objects.get(pk=module_id)
    comment_parent = Comments.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author=request.user,
                id_record=record_id,
                parent=comment_parent,
                description=form.cleaned_data['description'],
                module_name=module,
                status=True,
            )
            comment.save()
            return redirect_by_module_record_id(request, record_id, module_id)


def delete_common_comment(request, comment_id):
    comment = Comments.objects.get(pk=comment_id)
    record_id = comment.id_record
    module_id = comment.module_name.pk
    comment.delete()
    return redirect_by_module_record_id(request, record_id, module_id)


def delete_common_comments_by_record(record_id, module_id):
    module = ModuleName.objects.get(pk=module_id)
    comments = Comments.objects.filter(id_record=record_id, module_name=module)
    comments.delete()
    return None


def redirect_by_module_record_id(request, record_id, module_id):
    if (module_id == 1):
        return redirect(reverse('projects_task_detail', kwargs={'task_id': record_id}))
    elif (module_id == 3):
        model = TaskApproveStatusActions.objects.get(pk=record_id)
        return redirect(reverse('projects_task_detail', kwargs={'task_id': model.task.pk}))
    else:
        context = {
            'id': module_id
        }
        return render(request, 'todo/todo_cher.html', context)