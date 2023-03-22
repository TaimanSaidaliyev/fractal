from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ViewToDiListAll, name='todo'),
    path('json', view_tasks_json, name='todo_json'),
    path('add', add_todo, name='add_todo'),
    path('detail/<int:pk>', ViewTodo, name='todo_detail'),
    path('update/<int:pk>', update_todo, name='todo_update'),
    path('delete/<int:pk>', DeleteTodo, name='todo_delete'),
    path('delete_file/<int:pk>', delete_file, name='todo_file_delete'),
    path('cher', cher, name='cher')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

