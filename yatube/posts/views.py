from django.shortcuts import render, get_object_or_404
from .models import Group, Post
POSTS_ON_PAGE = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related()[:POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
