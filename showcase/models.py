from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    profile_image = models.ImageField (upload_to="profile_images/",null=True,blank=True)

    def __str__(self):
        return self.name


class UserProject(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=200)
    image = models.ImageField (upload_to="media/project_images/",null=True,blank=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


