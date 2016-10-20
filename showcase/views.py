from django.shortcuts import render
from showcase.models import UserProfile

def student_list(request):
    student = UserProfile.objects.all
    context_dict = {'students': student }
    return render(request, 'showcase/student_list.html', context_dict)
