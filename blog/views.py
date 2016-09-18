from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def index(request):
    category_list = Category.objects.order_by('name')
    posts_lists = Post.objects.order_by('-published_date')
    query = request.GET.get("q")
    if query:
        posts_lists = posts_lists.filter(Q(title__icontains=query)|Q(text__icontains=query)).distinct()
    paginator = Paginator(posts_lists, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    context_dict = {'categories': category_list, 'posts': posts }
    return render(request, 'blog/post_list.html', context_dict)


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
    return render(request, 'blog/category.html', context_dict)

def post_detail(request, post_title_slug):
    post = Post.objects.get(slug=post_title_slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def register(request):
   if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           new_user = form.save()
           return HttpResponseRedirect("/login")
   else:
       form = UserCreationForm()
   return render(request, "users/register.html", {
       'form': form,
   })