from django import forms
from .models import UserProfile
from showcase.models import UserProject

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "name",
            "profile_image",
        ]

class UserProjectForm(forms.ModelForm):
    class Meta:
        model = UserProject
        fields = [
            "title",
            "image",
            "description",
            "url",
        ]
