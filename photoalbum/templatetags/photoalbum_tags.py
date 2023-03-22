from django import template

from photoalbum.forms import AddPhotoAlbumItem
from photoalbum.models import PhotoAlbume, PhotoAlbumeCategory, PhotoAlbumeItem

register = template.Library()


@register.inclusion_tag('photoalbum/widgets/small/photoalbum_card.html')
def show_photoalbum_card(photoalbum_id):
    album = PhotoAlbume.objects.get(pk=photoalbum_id)
    context = {
        'album': album,
    }
    return context


@register.inclusion_tag('photoalbum/widgets/main/photoalbum_list.html')
def show_photoalbum_list():
    albums = PhotoAlbume.objects.all()
    context = {
        'albums': albums
    }
    return context


@register.inclusion_tag('photoalbum/widgets/main/photoalbum_list.html')
def show_photoalbum_list_by_category(category_id):
    category = PhotoAlbumeCategory.objects.get(pk=category_id)
    albums = PhotoAlbume.objects.filter(category=category)
    context = {
        'albums': albums
    }
    return context


@register.inclusion_tag('photoalbum/widgets/main/photoalbum_mainpage_header.html')
def show_photoalbum_mainpage_header(request, category_id):
    context = {
        'request': request,
        'category_id': category_id,
    }
    return context


@register.inclusion_tag('photoalbum/widgets/main/photoalbum_categories_horizontal.html')
def show_photoalbum_categories_horizontal(request, category_id):
    categories = PhotoAlbumeCategory.objects.filter(company=request.user.profile.company.pk)
    context = {
        'categories': categories,
        'category_id': category_id
    }
    return context


@register.inclusion_tag('photoalbum/widgets/small/photoalbum_item.html')
def show_photoalbum_item(image_id):
    image = PhotoAlbumeItem.objects.get(pk=image_id)
    context = {
        'image': image,
    }
    return context


@register.inclusion_tag('photoalbum/widgets/small/photoalbum_items_header.html')
def show_photoalbum_items_header(photoalbum_id):
    photoalbum = PhotoAlbume.objects.get(pk=photoalbum_id)
    photoalbum_items = PhotoAlbumeItem.objects.filter(photoalbum=photoalbum_id)
    context = {
        'photoalbum': photoalbum,
        'photoalbum_items_count': photoalbum_items.count()
    }
    return context


@register.inclusion_tag('photoalbum/widgets/small/photoalbum_upload_item.html')
def show_photoalbum_item_upload(photoalbum_id):
    photoalbum = PhotoAlbume.objects.get(pk=photoalbum_id)
    form = AddPhotoAlbumItem()
    context = {
        'upload_items_form': form,
        'photoalbum': photoalbum,
    }

    return context


@register.tag
def is_url_photoalbum_image_empty(url):
    altenative_image = '123'
    if url:
        return url
    else:
        return altenative_image

