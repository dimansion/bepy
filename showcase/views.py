from django.shortcuts import render
from showcase.models import UserProfile, UserProject

def student_list(request):
    student = UserProfile.objects.all
    context_dict = {'students': student }
    return render(request, 'showcase/student_list.html', context_dict)

def student_detail(request, user_slug):
    projects = UserProfile.objects.get(slug=user_slug)
    project_list = UserProject.objects.filter(project=projects)
    return render(request, 'showcase/student_detail.html', {'projects': projects, 'project_lists':project_list,})

