from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import UserProfile
from showcase.models import UserProject
from .forms import UserProfileForm, UserProjectForm
from django.contrib.auth.decorators import login_required

# my profile asosiated
@login_required
def user_dashboard(request):
    user = request.user
    userdetail = UserProfile.objects.get(user=user)
    context_dict={ "user":user, 'userdetails':userdetail }
    return render(request, 'dashboard/user.html', context_dict)

@login_required
def user_update(request, slug=None):
    #if not request.user.is_staff or not request.user.is_superuser:
    #    raise Http404
    instance = get_object_or_404(UserProfile, slug=slug)
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('dashboard:user_dashboard')

    context_dict = {
        "instance": instance,
        "form":form,
    }
    return render(request, 'dashboard/user_update.html', context_dict)

# my projects asosiated
def add_project(request):
    user = request.user
    userdetail = UserProfile.objects.get(user=user)
    form = UserProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.project = userdetail
        instance.save()

        return redirect('dashboard:projects')
    context = {
        "form": form,
    }
    return render(request, "dashboard/add_project.html", context)

@login_required
def user_project(request):
    user = request.user
    projects = UserProfile.objects.get(user=user)
    project_list = UserProject.objects.filter(project=projects)
    context_dict = {'projects': projects, 'project_lists':project_list,}
    return render(request, 'dashboard/user_project.html', context_dict)

def user_project_detail(request, user_project_slug):
    user = request.user
    projects_student = UserProfile.objects.get(user=user)
    student_project = UserProject.objects.get(slug=user_project_slug)
    project_detail = UserProject.objects.all()
    context_dict = {'student_projects': student_project, 'project_details': project_detail, 'projects_student': projects_student}
    return render(request, 'dashboard/project_detail.html', context_dict)

def user_project_update(request, slug=None):
    instance = get_object_or_404(UserProject, slug=slug)
    form = UserProjectForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('dashboard:project_detail', slug)

    context_dict = {
        "title": instance.title,
        "instance": instance,
        "form":form,
    }
    return render(request, 'dashboard/user_update.html', context_dict)

def user_project_delete(request, slug=None):
    instance = get_object_or_404(UserProject, slug=slug)
    instance.delete()
    return redirect('dashboard:projects')
