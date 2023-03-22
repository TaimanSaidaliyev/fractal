from django import template
from common_settings.models import UserTemplate
from mysite.settings import MEDIA_URL

register = template.Library()


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_sidebar_type(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)

    ret_r = interface_parameters.sidebar.sidebar_style
    return {"interface_parameters": ret_r}


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_logo_sidebar(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)

    if (interface_parameters.sidebar_id == 1):
        ret_r = interface_parameters.logo_light
    else:
        ret_r = interface_parameters.logo_dark
    return {"interface_parameters": ret_r}


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_logo(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)
    ret_r = interface_parameters.photo
    return {"interface_parameters": ret_r}


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_background(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)
    ret_r = interface_parameters.background_theme
    return {"interface_parameters": str(MEDIA_URL) + str(ret_r)}


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_header_type(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)

    ret_r = interface_parameters.header.header_style
    return {"interface_parameters": ret_r}


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_content_type(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)

    ret_r = interface_parameters.content_type.content_style
    return {"interface_parameters": ret_r}


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_is_sidebar_top(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)

    ret_r = interface_parameters.is_sidebar.is_sidebar_top
    return {"interface_parameters": ret_r}


@register.inclusion_tag('common_settings/widgets/interface_parameters.html')
def show_is_sidebar_left(user):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=user)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)

    ret_r = interface_parameters.is_sidebar.is_sidebar_left
    return {"interface_parameters": ret_r}


@register.inclusion_tag('common_settings/widgets/top_menu.html')
def show_top_menu(request):
    try:
        interface_parameters = UserTemplate.objects.get(user_id=request.user.pk)
    except:
        interface_parameters = UserTemplate.objects.get(pk=1)

    ret_r = interface_parameters.is_sidebar.pk
    if (ret_r == 2):
        ret_r = True
    else:
        ret_r = False

    context = {
        'request': request,
        'ret_r': ret_r,
    }
    return context

