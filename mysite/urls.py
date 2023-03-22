from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .view import error_404
from news.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('start_page.urls')),
    path('main/', include('news.urls')),
    path('todo/', include('todo.urls')),
    path('profile/', include('profile_add.urls')),
    path('updated_interface/', include('common_settings.urls')),
    path('menu/', include('menu.urls')),
    path('chat/', include('chat.urls')),
    path('user/', include('start_page.urls')),
    path('proj_man/', include('proj_man.urls')),
    path('common/', include('common.urls')),
    path('404', error_404, name='error_404'),
    path('photoalbum/', include('photoalbum.urls'), name='photoalbum')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)