import os
import pathlib

from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

import todo
from .forms import ToDoForm
from .models import ToDo, Files, FileIcon, PriorityToDo
from django.views.generic import ListView, DetailView, CreateView
from .forms import ToDoForm, FileForm
from django.contrib import auth
from django.urls import reverse
import datetime



def ViewToDiListAll(request):
    list_todo = ToDo.objects.filter(author=request.user)
    context = {
        'name': 'Taiman',
        'list_todo': list_todo,
    }
    template = 'todo/todo_list.html'
    return render(request, template, context)


def ViewTodo(request, pk):
    try:
        todo_check = ToDo.objects.get(pk=pk)
    except:
        return redirect('error_404')
    if (todo_check.author == request.user):
        #Уведомление о том что запись обновлена из функции update_todo
        try:
            if (request.session['updated'] > 0):
                if 'updated' in request.session:
                    del request.session['updated']
        except:
            None

        todo = ToDo.objects.get(pk=pk)
        files = Files.objects.filter(todo_relate=pk)
        context = {
            'name': 'Детальное описание',
            'todo': todo,
            'files': files
        }
        template = 'todo/todo_detail.html'
        return render(request, template, context)
    return redirect('error_404')


def DeleteTodo(request, pk):
    lavina = ''
    files = Files.objects.filter(todo_relate=pk)
    for file in files:
        file_name = os.remove("media/" + str(file.attached_file))

    context = {
        'files': file_name,
    }

    todo = ToDo.objects.get(pk=pk)
    todo.delete()
    return redirect('todo')


def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        file_form = FileForm()
        files = request.FILES.getlist('attached_file')
        if form.is_valid():
            model = form.save()
            todo_id = ToDo.objects.get(pk=model.pk)
            for file in files:
                file_name = os.path.basename("media/" + str(file))
                file_extension = pathlib.Path(file_name).suffix
                try:
                    icon_id = FileIcon.objects.filter(suffix=file_extension).first()
                    new_files = Files(
                        todo_relate=todo_id,
                        attached_file=file,
                        icon_id=icon_id.pk,
                    )
                except:
                    new_files = Files(
                        todo_relate=todo_id,
                        attached_file=file,
                        icon_id=1,
                    )
                new_files.save()
            return redirect(reverse('todo_detail', kwargs={'pk': todo_id.pk}))
    else:
        form = ToDoForm()
        file_form = FileForm()
    return render(request, 'todo/todo_add.html', {'todo': form, 'file_form': file_form, 'type': 'add_todo'})


def update_todo(request, pk):
    #Открываем сессию для уведомления о том что запись успешна обновлена
    request.session['updated'] = 0
    todo = ToDo.objects.get(pk=pk)
    template = 'todo/todo_add.html'
    context = {
        'todo_main': todo,
        'update': True,
        'type': 'update_todo',
        'todo': ToDoForm(instance=todo),
        'file_form': FileForm(),
    }
    if request.method == 'POST':
        form = ToDoForm(request.POST, request.FILES, instance=todo)
        files = request.FILES.getlist('attached_file')
        updated_success = 0
        if form.is_valid():
            for file in files:
                file_name = os.path.basename("media/" + str(file))
                file_extension = pathlib.Path(file_name).suffix
                try:
                    icon_id = FileIcon.objects.filter(suffix=file_extension).first()
                    new_files = Files(
                        todo_relate=todo,
                        attached_file=file,
                        icon_id=icon_id.pk,
                    )
                except:
                    new_files = Files(
                        todo_relate=todo,
                        attached_file=file,
                        icon_id=1,
                    )
                new_files.save()
            updated_success = 1
            form.save()
            return redirect(reverse('todo_detail', kwargs={'pk': pk}))
    return render(request, template, context)


def delete_file(request, pk):
    file = Files.objects.get(pk=pk)
    try:
        file_name = os.remove("media/" + str(file.attached_file))
    except:
        None
    file.delete()
    return redirect(reverse('todo_detail', kwargs={'pk':file.todo_relate.pk}))


def cher(request):
    return render(request, 'todo/todo_cher.html')


def view_tasks_json(request):
    data = list(PriorityToDo.objects.values())
    return JsonResponse(data, safe=False)