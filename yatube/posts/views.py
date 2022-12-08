from django.shortcuts import render, get_object_or_404
from .models import Group, Post


def index(request):
    POSTS_ON_PAGE = 10
    template = 'posts/index.html'
    posts = Post.objects.select_related()[:POSTS_ON_PAGE]
    group = 'Не получается сюда затащить номер группы'
    context = {
        'posts': posts,
        'group': group,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    context = {
        'group': group,
        'posts': posts,
        'text': title,
    }
    return render(request, template, context)
