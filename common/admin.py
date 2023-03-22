from django.contrib import admin
from .models import CommonFiles, ModuleName, FileIcon, Comments, Company


admin.site.register(CommonFiles)
admin.site.register(ModuleName)
admin.site.register(FileIcon)
admin.site.register(Comments)
admin.site.register(Company)