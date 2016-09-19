import datetime, random, hashlib
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from blog.models import Category, Post, UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from blog.forms import RegistrationForm
from django.contrib.auth.models import User
from django.core.context_processors import csrf 
from django.template import RequestContext
from django.utils import timezone



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
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid(): 
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]            
            activation_key = hashlib.sha1((salt+email).encode('utf-8')).hexdigest()            
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
            user=User.objects.get(username=username)

            # Create and save user profile                                                                                                       
            new_profile = UserProfile(user=user, activation_key=activation_key, 
                key_expires=key_expires)
            new_profile.save()
            host=request.META['HTTP_HOST']

            # Send email with activation key
            email_subject = 'Aktivasi akun Be-Py'
            email_body = "Hey {}, Terima kasih telah mendaftar. \n Untuk aktivasi akun Anda, silahkan klik link di bawah ini \n http://{}/confirm/{}".format(username, host, activation_key)

            send_mail(email_subject, email_body, 'be-py@alviandk.com',
                [email], fail_silently=False)

            return HttpResponseRedirect('/register_success')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('users/register.html', args, context_instance=RequestContext(request))

def confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('/blog')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('user_profile/confirm_expired.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    return render_to_response('users/confirm.html')


def register_success(request):    
    
    return render_to_response('users/success.html')

