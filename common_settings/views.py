from django.shortcuts import render, redirect
from .forns import InterfaceUpdateForm
from .models import UserTemplate


def UpdateInterface(request):
    template = 'common_settings/update_interface.html'
    if (UserTemplate.objects.filter(user=request.user)):
        interface = UserTemplate.objects.filter(user=request.user).first()
    else:
        interface = UserTemplate.objects.get(pk = 1)
        new_template = UserTemplate(
            user_id = request.user.id,
            template_type_id = interface.template_type_id,
            title = 'New',
            sidebar_id = interface.sidebar_id,
            header_id = interface.header_id,
            content_type = interface.content_type,
            is_sidebar_id = interface.is_sidebar_id,
            logo_dark = interface.logo_dark,
            logo_light = interface.logo_light, photo = interface.photo)
        new_template.save()

    context = {
        'interface': interface,
        'updated': False,
        'form': InterfaceUpdateForm(instance=interface),
    }

    if request.method == 'POST':
        form = InterfaceUpdateForm(request.POST, request.FILES, instance=interface)
        if form.is_valid():
            form.save()
            context['updated'] = True
            context['form'] = InterfaceUpdateForm(instance=interface)

    return render(request, template, context)


