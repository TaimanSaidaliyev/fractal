from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:record_id>/delete_file/<int:file_id>', delete_common_file, name='delete_file_by_record'),
    path('<int:record_id>/<int:module_id>/add_comment', add_common_comment, name='add_common_comment'),
    path('<int:record_id>/<int:module_id>/<int:comment_id>/reply_comment', reply_common_comment, name='reply_common_comment'),
    path('<int:comment_id>/delete_comment', delete_common_comment, name='delete_common_comment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)