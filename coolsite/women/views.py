from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = ['Про сайт', 'Добавити пост  ', 'Зворотній звязок', 'Вхід']

def index(request):
    posts = Women.objects.all()
    contest = {
        'posts': posts,
        'menu': menu,
        'title': 'Головна сторінка'
    }

    return render(request, 'women/index.html', contest)

def about(request):
    return render(request, 'women/about.html')

def categories(request, cat):
    return HttpResponse(f"<h1> Category  {cat} </h1>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('h1>Стор    інка не зайдена</h1>')