from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', photoalbum_list, name='photoalbum_list'),
    path('add/', photoalbum_add, name='photoalbum_add'),
    path('update/<int:photoalbum_id>', photoalbum_update, name='photoalbum_update'),
    path('delete/<int:photoalbum_id>', photoalbum_delete, name='photoalbum_delete'),
    path('category/<int:category_id>', photoalbum_by_category, name='photoalbum_by_category'),
    path('album/<int:photoalbum_id>', photoalbum_items, name='photoalbum_items'),
    path('album/edit/<int:photoalbum_id>', photoalbum_items_edit_mode, name='photoalbum_items_edit_mode'),
    path('item/delete/<int:photoalbum_item_id>', photoalbum_delete_item, name='photoalbum_item_delete'),
    path('upload/photoalbum/<int:photoalbum_id>', photoalbum_upload_items, name='photoalbum_upload_items'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)