from django import template
from common.models import CommonFiles, Comments
from common.forms import FileForm
from django.db.models import *


register = template.Library()


@register.inclusion_tag('common/widgets/module_record_files.html')
def show_module_record_files(request, record_id):
    is_exist = False
    files = CommonFiles.objects.filter(id_record=record_id)
    if (files.count() > 0):
        is_exist = True
    context = {
        'record_id': record_id,
        'files': files,
        'is_exist': is_exist,
    }
    return context


@register.inclusion_tag('common/widgets/module_record_files_list_small.html')
def show_module_record_files_list_small(request, record_id):
    return show_module_record_files(request, record_id)
