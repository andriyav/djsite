from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from .forms import AddPostForm
from .models import *


def index(request):
    posts = Women.objects.all()
    contexst = {
        'posts': posts,
        'title': 'Головна сторінка',
        'cat_selected': 0
    }

    return render(request, 'women/index.html', contexst)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()
    contexst = {
        'posts': posts,
        'title': 'Головна сторінка',
        'cat_selected': cat_id
    }

    return render(request, 'women/index.html', contexst)


def add_page(request):

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            form = AddPostForm()


    return render(request, 'women/addpage.html', {'form': form, 'title': 'Добавити статтью'})


def about(request):
    return render(request, 'women/about.html')


def contact(request):
    return render(request, 'women/about.html')


def login(request):
    return render(request, 'women/about.html')


def pageNotFound(request, exeption):
    return HttpResponseNotFound('h1>Стор    інка не зайдена</h1>')


def show_post(request, cat_id):
    return HttpResponse(f'page number {cat_id}')
