from django.http import HttpResponse, HttpResponseNotFound
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
        'title': 'Головна сторінка'
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


def show_post(request, post_id):
    return HttpResponse(f'page number {post_id}')

def categories(request, cat):
    return HttpResponse(f"<h1> Category  {cat} </h1>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('h1>Стор    інка не зайдена</h1>')