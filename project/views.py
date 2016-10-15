from django.shortcuts import render
from project.models import Page, Content
from django.views.generic import TemplateView

class ProjectView(TemplateView):
    template_name = "project/project.html"    

def page_list(request):
    posts = Page.objects.all
    context_dict = {'posts': posts }
    return render(request, 'project/post_list.html', context_dict)

def page_detail(request, page_title_slug):
    post = Page.objects.get(slug=page_title_slug)
    lesson_list = Content.objects.filter(lesson=post)
    return render(request, 'project/post_detail.html', {'post': post, 'lesson_list':lesson_list,})

def lesson_detail(request, lesson_name_slug):
    lessons = Content.objects.get(slug=lesson_name_slug)
    lessons_detail = Content.objects.all()
    return render(request, 'project/lesson_detail.html', {'lessons': lessons, 'lessons_detail': lessons_detail})
