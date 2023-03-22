from django.contrib import admin
from .models import ToDo, PriorityToDo, Status, Files, FileIcon


class PriorityToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(ToDo)
admin.site.register(PriorityToDo, PriorityToDoAdmin)
admin.site.register(Status)
admin.site.register(Files)
admin.site.register(FileIcon)

