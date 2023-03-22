from django.contrib import admin
from .models import Project, Tasks, TimeTracking, Status, Priority, Category, UserSelfCategory, \
    UserSelfCategoryDictionary, UserSelfSavedTasks, TaskChangeHistory, TaskChangeHistoryAction, TaskApproveStatus, TaskApproveStatusActions, TaskAnswerByExecutors


admin.site.register(Project)
admin.site.register(Tasks)
admin.site.register(TimeTracking)
admin.site.register(Status)
admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(UserSelfCategory)
admin.site.register(UserSelfCategoryDictionary)
admin.site.register(UserSelfSavedTasks)
admin.site.register(TaskChangeHistory)
admin.site.register(TaskChangeHistoryAction)
admin.site.register(TaskApproveStatus)
admin.site.register(TaskApproveStatusActions)
admin.site.register(TaskAnswerByExecutors)
