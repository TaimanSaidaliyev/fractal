from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('news/', main_page, name='home'),
    path('news/all', HomeNews.as_view(), name='all_news'),
    #path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(extra_context={'title_page':'Категории'}), name='category'),
    path('savednews/<int:user_id>/', NewsBySaved.as_view(extra_context={'title_page':'Сохраненные записи'}), name='savednews'),
    path('likednews/<int:user_id>/', NewsByLiked.as_view(extra_context={'title_page': 'Понравившиеся записи'}), name='likednews'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/<int:pk>/updated/<int:updated_success>', HomeNews.as_view(extra_context={'updated_success':'Yes'}), name='view_news_updated'),
    path('news/<int:pk>/delete_new', DeleteNews, name='delete_new'),
    path('delete_comments/<int:pk>', DeleteComments, name='delete_comments'),
    path('news/add-news', CreateNews.as_view(), name='add_news'),
    path('news/<int:pk>/add-news/<int:added_news_success>', ViewNews.as_view(extra_context={'added_news_success':'Yes'}), name='added_news'),
    path('news/<int:pk>/add-comment/<int:added_comment_success>', ViewNews.as_view(extra_context={'added_comment_success':'Yes'}), name='added_comment'),
    path('news/<int:pk>/update_news', UpdateNews, name='update_news'),
    path('news/like/<int:pk>/<int:id>', NewsLike, name='news_like'),
    path('news/save/<int:pk>/<int:id>', NewsSaveView, name='news_save'),
    path('news/register', register, name='register'),
    path('news/login', user_login, name='login'),
    path('logout', user_logout, name='logout')
]