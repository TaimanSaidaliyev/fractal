from django.contrib import admin
from .models import UserTemplate, SidebarType, HeaderType, ContentType, TemplateType, IsSidebar


admin.site.register(UserTemplate)
admin.site.register(SidebarType)
admin.site.register(HeaderType)
admin.site.register(ContentType)
admin.site.register(TemplateType)
admin.site.register(IsSidebar)
