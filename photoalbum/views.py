import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AddPhotoAlbume, AddPhotoAlbumItem
from .models import PhotoAlbume, PhotoAlbumeCategory, PhotoAlbumeItem
from common.models import User
from django.urls import reverse
from imagekit.utils import get_cache
from common.models import Company
from django.views.generic import ListView


def photoalbum_list(request):
    template = 'photoalbum/photoalbum_mainpage.html'
    page_type = 'photoalbum_list_all'
    model = PhotoAlbume.objects.all()
    context = {
        'albums': model,
        'page_type': page_type
    }
    return render(request, template, context)


def photoalbum_items(request, photoalbum_id):
    template = 'photoalbum/photoalbum_items.html'
    page_type = 'photoalbum_items_list'
    photoalbum = PhotoAlbume.objects.get(pk=photoalbum_id)
    model = PhotoAlbumeItem.objects.filter(photoalbum=photoalbum_id)
    form = AddPhotoAlbumItem()
    context = {
        'page_type': page_type,
        'photoalbum_items': model,
        'photoalbum': photoalbum,
        'upload_items_form': form,
    }
    return render(request, template, context)


def photoalbum_items_edit_mode(request, photoalbum_id):
    template = 'photoalbum/photoalbum_items_edit.html'
    page_type = 'photoalbum_items_edit_mode'
    photoalbum = PhotoAlbume.objects.get(pk=photoalbum_id)
    model = PhotoAlbumeItem.objects.filter(photoalbum=photoalbum_id)
    form = AddPhotoAlbumItem()
    if request.method == 'POST':
        items = request.POST.getlist('items')
        for item in items:
            try:
                photoalbum_delete_item(request, item)
            except:
                None
    context = {
        'page_type': page_type,
        'photoalbum_items': model,
        'photoalbum': photoalbum,
        'upload_items_form': form,
    }
    return render(request, template, context)


def photoalbum_add(request):
    template = 'photoalbum/photoalbum_add_edit.html'
    type = 'photoalbum_add'
    form = AddPhotoAlbume(request.POST, request.FILES)
    model = PhotoAlbume()
    company = Company.objects.get(pk=request.user.profile.company.pk)
    if (request.method == 'POST'):
        if form.is_valid():
            try:
                model = PhotoAlbume(
                    title=form.cleaned_data['title'],
                    author=request.user,
                    category=form.cleaned_data['category'],
                    event_at=form.cleaned_data['event_at'],
                    event_description=form.cleaned_data['event_description'],
                    image=request.FILES.get('photoalbum_image'),
                    company=company,
                )
                model.save()
                return redirect(reverse('photoalbum_list'))
            except:
                return HttpResponse('Error')
    context = {
        'form': form,
        'page_type': type,
    }
    return render(request, template, context)


def photoalbum_update(request, photoalbum_id):
    template = 'photoalbum/photoalbum_add_edit.html'
    type = 'photoalbum_update'
    model = PhotoAlbume.objects.get(pk=photoalbum_id)
    form = AddPhotoAlbume(instance=model)
    company = Company.objects.get(pk=request.user.profile.company.pk)
    if (request.method == 'POST'):
        form = AddPhotoAlbume(request.POST, request.FILES, instance=model)
        if form.is_valid():
            model.title=form.cleaned_data['title']
            model.author=request.user
            model.category=form.cleaned_data['category']
            model.event_at=form.cleaned_data['event_at']
            model.event_description=form.cleaned_data['event_description']
            model.image=request.FILES.get('photoalbum_image')
            model.company=company
            model.save()
    context = {
        'photoalbum': model,
        'form': form,
        'page_type': type
    }
    return render(request, template, context)


def photoalbum_delete(request, photoalbum_id):
    if (request.method == 'POST'):
        type = 'photoalbum_delete'
        model = PhotoAlbume.objects.get(pk=photoalbum_id)
        items = PhotoAlbumeItem.objects.filter(photoalbum=photoalbum_id)
        for item in items:
            try:
                os.remove("media/" + str(item.image))
            except:
                None
        try:
            os.remove("media/" + str(model.image))
        except:
            None
        model.delete()
        get_cache().clear()
    return redirect(reverse('photoalbum_list'))


def photoalbum_by_category(request, category_id):
    template = 'photoalbum/photoalbum_mainpage.html'
    page_type = 'photoalbum_list_by_category'
    category = PhotoAlbumeCategory.objects.get(pk=category_id)
    context = {
        'category': category,
        'page_type': page_type,
        'category_id': category_id
    }

    return render(request, template, context)


def photoalbum_upload_items(request, photoalbum_id):
    photoalbum = PhotoAlbume.objects.get(pk=photoalbum_id)
    success = True
    if request.method == 'POST':
        files = request.FILES.getlist('image')
        for file in files:
            model = PhotoAlbumeItem(
                photoalbum=photoalbum,
                author=request.user,
                image=file,
            )
            model.save()
    return redirect(reverse('photoalbum_items', kwargs={'photoalbum_id': photoalbum_id}))


def photoalbum_delete_item(request, photoalbum_item_id):
    item = PhotoAlbumeItem.objects.get(pk=photoalbum_item_id)
    if(request.method == 'POST'):
        try:
            item.delete()
            os.remove("media/" + str(item.image))
        except:
            None
    return redirect(reverse('photoalbum_items', kwargs={'photoalbum_id': item.photoalbum.pk}))

