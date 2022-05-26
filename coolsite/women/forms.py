from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок")
    slug = forms.SlugField(max_length=255, label="Посилання")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':10}), label="Контент")
    is_published = forms.BooleanField(label="Публикація", initial=True, required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категорія", empty_label="Виберіть категорію")