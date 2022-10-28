from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User


def index(request):
    posts = Post.objects.select_related('group')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'for_loop': 'includes/for_loop.html',
        'paginator': 'includes/paginator.html',
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('group')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'for_loop': 'includes/for_loop.html',
        'paginator': 'includes/paginator.html',
        'page_obj': page_obj
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    all_posts = author.posts.all()
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
        'paginator': 'includes/paginator.html',
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    author = post.author
    count = Post.objects.filter(author=author).count()
    context = {
        'post': post,
        'count': count,
        'author': author
    }
    return render(request, 'posts/post_detail.html', context)
