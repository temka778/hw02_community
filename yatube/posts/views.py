from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


#COUNT_OF_POSTS = 10


def index(request):
    posts = Post.objects.select_related('group')#[:COUNT_OF_POSTS]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'for_loop': 'includes/for_loop.html',
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('group')#[:COUNT_OF_POSTS]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'for_loop': 'includes/for_loop.html',
        'page_obj': page_obj
    }
    return render(request, 'posts/group_list.html', context)
