from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import AddPostForm
from .models import *
# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
#         ]

# def index(request):
#     posts = Women.objects.all()
#     contexst = {
#         'posts': posts,
#         'title': 'Головна сторінка',
#         'cat_selected': 0
#     }
#
#     return render(request, 'women/index.html', contexst)
class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна сторінка'
        context['cat_selected'] = 0

        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)

class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категорія - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#     contexst = {
#         'posts': posts,
#         'title': 'Головна сторінка',
#         'cat_selected': cat_id
#     }
#
#     return render(request, 'women/index.html', contexst)


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def show_post(request, cat_id):
    return HttpResponse(f'page number {cat_id}')


def about(request):
    return render(request, 'women/about.html')


def contact(request):
    return render(request, 'women/about.html')


def login(request):
    return render(request, 'women/about.html')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('h1>Стор    інка не зайдена</h1>')



