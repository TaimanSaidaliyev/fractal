from django import template

from news.models import Category, News
from alerts.models import AlerstList
from django.db.models import *
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag(name='get_alerts_list')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('alerts/alerts.html')
def show_alerts(confirm=None):
    message = AlerstList.objects.get(url_name=confirm)
    return {"alerts": message.description}