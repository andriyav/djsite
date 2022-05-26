from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()
    contexst = {
        'posts': posts,
        'menu': menu,
        'title': 'Головна сторінка',
        'cat_selected': 0
    }

    return render(request, 'women/index.html', contexst)

def about(request):
    return render(request, 'women/about.html')

def add_page(request):
    return render(request, 'women/about.html')

def contact(request):
    return render(request, 'women/about.html')

def login(request):
    return render(request, 'women/about.html')

def pageNotFound(request, exeption):
    return HttpResponseNotFound('h1>Стор    інка не зайдена</h1>')

def show_post(request, cat_id):

    return HttpResponse(f'page number {cat_id}')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    contexst = {
        'posts': posts,
        'menu': menu,
        'title': 'Головна сторінка',
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html', contexst)

