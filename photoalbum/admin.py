from django.contrib import admin
from .models import PhotoAlbume, PhotoAlbumeCategory, PhotoAlbumeItem

admin.site.register(PhotoAlbume)
admin.site.register(PhotoAlbumeCategory)
admin.site.register(PhotoAlbumeItem)
