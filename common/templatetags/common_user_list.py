from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.inclusion_tag('common/widgets/user_small_balls_list.html')
def show_user_small_balls_list(request, user_list, user_max_count):
    user_list = user_list
    user_many = False
    user_one = False
    if (user_list.count() > user_max_count):
        user_many = True
    if (user_list.count() <= 1):
        user_one = True

    context = {
        'user_list': user_list[:user_max_count],
        'user_many': user_many,
        'user_count': user_list.count() - user_max_count,
        'user_one': user_one,
    }
    return context


def show_user_information(request, user_id):
    user = User.objects.get(pk=user_id)
    return user


@register.inclusion_tag('common/widgets/user_info_small_circle_35.html')
def show_user_small_ball_50(request, user_id):
    context = {
        'user': show_user_information(request, user_id)
    }
    return context
