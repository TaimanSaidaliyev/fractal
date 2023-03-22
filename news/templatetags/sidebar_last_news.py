from django import template

from news.models import Category, News
from django.db.models import *
register = template.Library()


#Здесь создаем тэг, который будет передавать параметры в HTML страницы, которые запросили эту функцию.
#К примеру функция get_categories передает все Категории в страницу mysite/templates/inc/_sidebar/category.html
#под названием get_list_categories
@register.simple_tag(name='get_list_news')
def get_news():
    return News.objects.all()


#Эта функция передает в определенный файл свои параметры И его можно вызвать на людой странице, это что-то вроде виджета
@register.inclusion_tag('news/widgets/sidebar_last_news.html')
def show_sidebar_news(arg1='Hello', arg2='world'):
    #categories = Category.objects.all()
    news_t = News.objects.filter(is_published = True)[:5]
    return {"last_news": news_t, "arg1": arg1, "arg2": arg2}