from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
import datetime
from time import strftime
from .models import Department, StartDay, TimeTrackingProperties, JustTest
from django.http import JsonResponse
import json

def ProfilePage(request):
    template = 'profile_add/profile.html'
    user_form = UserForm()
    profile_form = ProfileForm()
    return render(request, template,
    {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
@transaction.atomic
def update_profile(request, pk=None):
    if (pk):
        profile_user = User.objects.get(pk=pk)
        profile_add = Profile.objects.get(user_id=pk)
    else:
        profile_user = User.objects.get(pk=request.user.pk)
        profile_add = Profile.objects.get(user_id=request.user.pk)

    context = {
        'user_form': UserForm(instance=profile_user),
        'updated': False,
        'profile_form': ProfileForm(instance=profile_add),
        'user_data': profile_user,
        'profile_data': profile_add,
    }

    if request.method == 'POST':
        profile_user_form = UserForm(request.POST, request.FILES, instance=profile_user)
        profile_add_form = ProfileForm(request.POST, request.FILES, instance=profile_add)
        if profile_user_form.is_valid() and profile_add_form.is_valid():
            profile_user_form.save()
            profile_add_form.save()
            context['updated'] = True
            context['user_form'] = UserForm(instance=profile_user)
            context['profile_form'] = ProfileForm(instance=profile_add)

    return render(request, 'profile_add/profile_edit.html', context)


def view_profile(request, pk):
    template = 'profile_add/profile_view.html'
    profile = User.objects.get(pk=pk)
    profile_add = Profile.objects.get(user_id=pk)

    context = {
        'id': profile_add.user_id,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'fathers_name': profile_add.fathers_name,
        'email': profile.email,
        'person_id': profile_add.person_id,
        'birth_date': profile_add.birth_date,
        'start_date': profile_add.start_date,
        'photo': profile_add.photo,
        'education': profile_add.education,
        'location': profile_add.location,
        'telephone': profile_add.telephone,
        'telephone_job': profile_add.telephone_job,
        'skype': profile_add.skype,
        'instagram': profile_add.instagram,
        'linkedin': profile_add.linkedin,
        'facebook': profile_add.facebook,
        'certificate': profile_add.certificate.all,
        'honor': profile_add.honor.all,
        'bio': profile_add.bio,
        'website': profile_add.website,
        'quote': profile_add.quote,
        'company': profile_add.company.description,
        'department': profile_add.department.description,
        'gender': profile_add.gender_id,
        'job_title': profile_add.job_title.description,
        'status': profile_add.status.description,
        'user_id': profile_add.user_id
    }

    return render(request, template, context)


def view_all_users(request):
    template = 'profile_add/profile_all_users.html'
    user = Profile.objects.get(user=request.user.pk)
    profiles = User.objects.filter(profile__company=user.company)
    department_ou = Department.objects.filter(company=user.company)
    context = {
        'user_p': profiles,
        'department_ou': department_ou,
    }

    return render(request, template, context)


def time_tracking(request):
    message = ''
    current_date = datetime.date.today()
    user_id = request.user.id
    next = request.POST.get('next', '/')
    record = StartDay.objects.get(user_id=user_id, date=current_date)
    if request.method == 'POST':
        if (record.is_ended):
            message = 'День уже завершен'
        else:
            if (record.is_working == False):
                record.start_time = strftime("%H:%M:%S")
                record.is_working = True
                record.save()
                message = 'День начался'
            else:
                record.end_time = strftime("%H:%M:%S")
                record.is_working = False
                record.is_ended = True
                record.save()
                message = 'День завершен'

    return HttpResponseRedirect(next)


def time_tracking_js(request):
    return render(request, 'profile_add/widgets/time_tracking_js.html')


def time_tracking_report(request):
    records = StartDay.objects.all()
    time_tracking_properties = TimeTrackingProperties.objects.get(company=1)
    context = {
        'records': records.order_by('date'),
        'time_tracking_properties': time_tracking_properties
    }
    return render(request, 'profile_add/time_tracking_report.html', context)


def api(request):
    new_field = list(JustTest.objects.values())
    return JsonResponse(new_field, safe=False)
