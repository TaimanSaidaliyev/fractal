from django import template
from common.models import Comments
from common.forms import CommentForm, FileForm


register = template.Library()

@register.inclusion_tag('common/widgets/user_comments.html')
def show_user_comments(request, record_id, module_id):
    comments = Comments.objects.filter(id_record=record_id, module_name=module_id, status=True)
    count = comments.count()
    form = CommentForm(request.POST)
    context = {
        'request': request,
        'comments': comments,
        'form': form,
        'module_id': module_id,
        'record_id': record_id,
    }
    return context