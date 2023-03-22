from django import template
from django.db.models import *
from profile_add.models import StartDay
import datetime
from django.shortcuts import render

register = template.Library()


@register.inclusion_tag('profile_add/widgets/time_tracking.html')
def show_time_tracking(request):
    current_date = datetime.date.today()
    user_id = request.user.id
    try:
        record = StartDay.objects.get(user=user_id, date=current_date)
    except:
        record = StartDay(user_id=user_id, date=current_date)
        record.save()
    context = {
        'record': record,
        'request': request,
    }

    return context