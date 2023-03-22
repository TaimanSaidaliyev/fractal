from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('project/<int:project_id>', view_tasks, name='projects_tasks_list'),
    path('project/add', add_project, name='project_add'),
    path('project/update/<int:project_id>', update_project, name='project_update'),
    path('project/delete/<int:project_id>', delete_project, name='project_delete'),
    path('project/delete_completely/<int:project_id>', delete_project_completely, name='project_delete_completely'),
    path('project/list', view_project_list, name='projects_list'),
    path('project/add_project_users/<int:project_id>', add_project_users, name='add_project_users'),
    path('project/main', view_project_my_tasks, name='project_main'),
    path('project/usercategory/<int:category_id>', view_project_tasks_by_user_self_category, name='project_userself_category'),
    path('project/saved_tasks', view_project_saved_tasks_by_user_self, name='project_userself_saved_tasks'),
    path('project/created_by_self_user', view_project_tasks_by_self_user, name='project_userself_created_tasks'),
    path('task/<int:task_id>', view_task_detail, name='projects_task_detail'),
    path('task/<int:project_id>/add', add_project_task, name='projects_task_add'),
    path('task/<int:project_id>/<int:task_id>/add', add_project_sub_task, name='projects_sub_task_add'),
    path('task/add', add_task, name='task_add'),
    path('task/update/<int:task_id>', update_task, name='projects_task_update'),
    path('task/<int:task_id>/delete', delete_task, name='projects_task_delete'),
    path('user_category/add', add_user_category, name='add_user_category'),
    path('user_category/<int:category_id>/delete', delete_user_category, name='delete_user_category'),
    path('user_category/<int:category_id>/rename', rename_user_category, name='rename_user_category'),
    path('task/<int:task_id>/save', save_task_user_self, name='projects_task_save'),
    path('task/viewers_task', view_project_viewers_task, name='view_viewers_task'),
    path('task/completed_tasks', view_project_completed_tasks, name='view_completed_tasks'),
    path('task/copy_tasks/<int:task_id>/<int:project_id>', copy_project_task, name='copy_project_task'),
    path('task/add_related_tasks/<int:task_id>', add_related_tasks, name='add_related_tasks'),
    path('task/<int:task_id>/timetracking/', add_time_tracking_by_task, name='add_time_tracking_by_task'),
    path('task/<int:task_id>/timetracking_multi/', add_time_tracking_by_task_multi, name='add_time_tracking_by_task_multi'),
    path('task/timetracking/<int:time_tracking_id>/delete', delete_time_tracking, name='delete_time_tracking'),
    path('task/approve/<int:task_id>/status/<int:current_status>', task_change_approve_status_view, name='task_change_approve_status'),
    path('task/deny/<int:task_id>/status/<int:current_status>', task_deny_approve_status_view, name='task_deny_approve_status'),
]