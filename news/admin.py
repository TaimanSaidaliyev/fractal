from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import News, Category, NewsLikes, NewsSave
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo_75')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content') #добавляет поле поиска в админке
    list_editable = ('is_published',) #редактируемое поле в режиме чтения
    list_filter = ('is_published', 'category') #фильтр справа

    # Эти поля отображаются на странице добавления новостей
    fields = ('title', 'category', 'content', 'photo', 'get_photo_100', 'is_published', 'views', 'created_at', 'updated_at')

    # Поля ниже исключает редактирование на странице добавления новостей
    readonly_fields = ('get_photo_100', 'views', 'created_at', 'updated_at')


    def get_photo_75(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75px">') #mark_sage отображает в HTML виде
        else:
            return 'фото нет'
        get_photo_75.short_description = 'Миниатюра' #задает наимнование столбца в админ панеле

    def get_photo_100(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100px">') #mark_sage отображает в HTML виде
        else:
            return 'фото нет'
        get_photo_100.short_description = 'Миниатюра' #задает наимнование столбца в админ панеле


admin.site.register(News, NewsAdmin)
admin.site.register(NewsLikes)
admin.site.register(NewsSave)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Панель администратора'
admin.site.site_header = 'Панель администратора'