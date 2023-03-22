import os.path
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .utils import MyMixin
from .models import News, Category, Comments, NewsLikes, NewsSave
from .forms import NewsForm, UserRegisterForm, UserLoginForm, CommentNews, NewsLikesForm, NewsSaveForm
from django.contrib.auth.mixins import LoginRequiredMixin #контроллер авторизации по миксинам
from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('home')


class HomeNews(MyMixin, ListView):
    model = News #вызываем модель новостей, чтоб отобразить данные на странице
    template_name = 'news/view_all_news.html' #здесь страницу которую хотим сформировать
    context_object_name = 'all_news' #переменная, которая передается в эту страницу

    #extra_context = {'title':'Главная страница'} #дополнительные переменные, которые передаются в страницу
    mixin_prop = 'hello world'
    paginate_by = 6

    #Функция для передачи переменных на страницу из супер класса
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        #context['mixin_prop'] = self.get_prop()
        return context

    #фнукция, для фильтрации данных из модели по определенным параметрам
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category') #select_related оптимизирует запрос SQL (пока не понял как это работает)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/view_all_news.html'
    context_object_name = 'all_news'
    allow_empty = False #метод вместо ошибочной категории 500 ошибки покажет 404
    paginate_by = 6
    #функция передает наименование Категории в переменную title
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_title'] = Category.objects.get(pk=self.kwargs['category_id'])
        context['page_type'] = 'NewsByCategory'
        context['count'] = News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category').count
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class NewsBySaved(ListView):
    model = News
    template_name = 'news/view_all_news.html'
    context_object_name = 'all_news'
    allow_empty = False #метод вместо ошибочной категории 500 ошибки покажет 404
    paginate_by = 6
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = User.objects.get(pk=self.kwargs['user_id'])
        context['count'] = News.objects.filter(saved_news__user_id=self.kwargs['user_id'], is_published=True).count
        context['page_type'] = 'NewsBySaved'
        return context

    def get_queryset(self):
        try:
            return News.objects.filter(saved_news__user_id=self.kwargs['user_id'], is_published=True)
        except:
            return News.objects.filter(saved_news__user_id=self.request.user, is_published=True)


class NewsByLiked(ListView):
    model = News
    template_name = 'news/view_all_news.html'
    context_object_name = 'all_news'
    allow_empty = False #метод вместо ошибочной категории 500 ошибки покажет 404
    paginate_by = 6
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = User.objects.get(pk=self.kwargs['user_id'])
        context['page_type'] = 'NewsByLiked'
        context['count'] = News.objects.filter(likes_new__user_id=self.kwargs['user_id'], is_published=True).count
        return context

    def get_queryset(self):
        return News.objects.filter(likes_new__user_id=self.kwargs['user_id'], is_published=True)


class FirstNew(MyMixin, ListView):
    model = News #вызываем модель новостей, чтоб отобразить данные на странице
    template_name = 'news/home_news_list.html' #здесь страницу которую хотим сформировать
    context_object_name = 'first_new' #переменная, которая передается в эту страницу
    #extra_context = {'title':'Главная страница'} #дополнительные переменные, которые передаются в страницу
    mixin_prop = 'hello world'
    paginate_by = 2

    #Функция для передачи переменных на страницу из супер класса
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        #context['mixin_prop'] = self.get_prop()
        return context

    #фнукция, для фильтрации данных из модели по определенным параметрам
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category') #select_related оптимизирует запрос SQL (пока не понял как это работает)


def main_page(request):
    paginate_by = 2
    homenews = News.objects.filter(is_published=True)[1:3]
    firstnew = News.objects.filter(is_published=True)[:1]
    lastnews = News.objects.filter(is_published=True)[4:7]
    topnews = News.objects.filter(is_published=True).order_by('-views')[:3]
    response_data = {
        'homenews': homenews,
        'firstnew': firstnew,
        'lastnews': lastnews,
        'topnews': topnews
    }

    return render(request, 'news/home_news_list.html', response_data)


class ViewNews(DetailView, FormMixin):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'
    form_class = CommentNews

    def get_success_url(self, **kwargs):
        return reverse_lazy('view_news', kwargs={'pk':self.get_object().id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.news = self.get_object()
        self.object.author = self.request.user
        added_comment_success = 1
        self.object.save()
        return redirect(reverse('added_comment', kwargs={'pk': self.object.news.pk, 'added_comment_success':added_comment_success}))
        #return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #Процесс определения поставил ли лайк текущий пользователь
        pk = self.get_object().id
        id = self.request.user.id
        is_liked = NewsLikes.objects.filter(news_id=pk, user_id=id)
        if(is_liked):
            context['is_liked'] = 'Yes'
        else:
            context['is_liked'] = 'No'
        #Процесс определения сохранили ли пользователь эту новость
        is_saved = NewsSave.objects.filter(news_id=pk, user_id=id)
        if (is_saved):
            context['is_saved'] = 'Yes'
        else:
            context['is_saved'] = 'No'
        #Подсчет количества просмотров
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category' : category})


# Класс ниже в автоматическом виде создает форму и метод запроса POST наследуя параметры из form.py, кроме этого джанго
# делает переход благодаря функции get_absolute_url из файла models.py
class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = 'home' #переадресовывает пользователя если не авторизован
    def get_success_url(self, **kwargs):
        return reverse_lazy('view_news', kwargs={'pk':self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        success = False
        if form.is_valid():
            success = True
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        added_news_success = 0
        self.object = form.save(commit=False)
        if (self.object.author):
            self.object.author = self.object.author
        else:
            self.object.author = self.request.user
        added_news_success = 1
        self.object.save()

        return redirect(reverse('added_news', kwargs={'pk':self.object.pk, 'added_news_success':added_news_success}))
    #raise_exception = True - вызывает ошибку 403


def UpdateNews(request, pk):
    get_news = News.objects.get(pk=pk)
    template = 'news/add_news.html'
    context = {
        'news': get_news,
        'update': True,
        'form': NewsForm(instance=get_news)
    }

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=get_news)
        updated_success = 0
        if form.is_valid():
            if(form.fields['author']):
                form.fields['author'] = request.user
            updated_success = 1
            form.save()
            return redirect(reverse('view_news_updated', kwargs={'pk':pk,'updated_success':updated_success}))
    return render(request, template, context)


def DeleteNews(request, pk):
    news = News.objects.get(pk=pk)
    news.delete()
    return redirect(reverse('all_news'))


def DeleteComments(request, pk):
    comments = Comments.objects.get(pk=pk)
    comments.delete()
    return redirect(reverse('view_news', kwargs={'pk':comments.news_id}))


def NewsLike(request, pk, id):
    form_class = NewsLikesForm
    news = pk
    user = id
    count = NewsLikes.objects.filter(news_id=news, user_id=user).count()
    if count == 0:
        newslike = NewsLikes(news_id=news, user_id=user)
        newslike.save()
    else:
        newslike_delete = NewsLikes.objects.filter(news_id=news, user_id=user)
        newslike_delete.delete()
    return redirect(reverse('view_news', kwargs={'pk':pk}))


def NewsSaveView(request, pk, id):
    form_class = NewsSaveForm
    news = pk
    user = id
    count = NewsSave.objects.filter(news_id = news, user_id  = user).count()
    if count == 0:
        newssave = NewsSave(news_id=news, user_id=user)
        newssave.save()
    else:
        newssave_delete = NewsSave.objects.filter(news_id = news, user_id  = user)
        newssave_delete.delete()
    return redirect(reverse('view_news', kwargs={'pk':pk}))