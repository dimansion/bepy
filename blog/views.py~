from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post

def index(request):
    category_list = Category.objects.order_by('name')
    posts = Post.objects.all
    context_dict = {'categories': category_list, 'posts': posts }
    return render(request, 'blog/index.html', context_dict)

def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        posts = Post.objects.filter(category=category)
        context_dict['posts'] = posts
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    # Go render the response and return it to the client.
    return render(request, 'blog/category.html', context_dict)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

