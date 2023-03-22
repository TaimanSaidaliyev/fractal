from django import template

from news.models import Category, News
from django.db.models import *
from django.contrib.auth.models import User


register = template.Library()

#Здесь создаем тэг, который будет передавать параметры в HTML страницы, которые запросили эту функцию.
#К примеру функция get_categories передает все Категории в страницу mysite/templates/inc/_sidebar/category.html
#под названием get_list_categories
@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


#Эта функция передает в определенный файл свои параметры И его можно вызвать на людой странице, это что-то вроде виджета
@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories, "arg1": arg1, "arg2": arg2}


@register.inclusion_tag('news/widgets/sidebar_categories.html')
def show_sidebar_categories(arg1='Hello', arg2='world'):
    news_t = News.objects.filter(is_published = True)
    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories, "arg1": arg1, "arg2": arg2}


@register.inclusion_tag('news/widgets/top_categories.html')
def show_top_categories():
    news_t = News.objects.filter(is_published = True)
    categories = Category.objects.annotate(cnt=Count('get_news', filter=F('get_news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories}

@register.tag
def show_news_like():
    return 123
