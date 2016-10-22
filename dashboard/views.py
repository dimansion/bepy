from django.shortcuts import render
from dashboard.models import UserProfile

def user_dashboard(request):
    user = request.user
    try:
        user = request.user
        userdetail = UserProfile.objects.filter(user=user)
    except:
        userdetail = None

    context_dict={ "user":user, 'userdetails':userdetail }
    return render(request, 'dashboard/user.html', context_dict)