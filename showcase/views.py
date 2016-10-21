from django.shortcuts import render
from showcase.models import UserProfile, UserProject

def student_list(request):
    student = UserProfile.objects.all
    context_dict = {'students': student }
    return render(request, 'showcase/student_list.html', context_dict)

def student_detail(request, user_slug):
    projects = UserProfile.objects.get(slug=user_slug)
    project_list = UserProject.objects.filter(project=projects)
    context_dict = {'projects': projects, 'project_lists':project_list,}
    return render(request, 'showcase/student_detail.html', context_dict)

def student_project_detail(request,user_slug, student_project_slug):
	projects_student = UserProfile.objects.get(slug=user_slug)
	student_project = UserProject.objects.get(slug=student_project_slug)
	project_detail = UserProject.objects.all()
	context_dict = {'student_projects': student_project, 'project_details': project_detail, 'projects_student': projects_student}
	return render(request, 'showcase/student_project.html', context_dict)
