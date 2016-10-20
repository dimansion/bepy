from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    profile_image = models.ImageField (upload_to="profile_images/",null=True,blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
            self.slug = slugify(self.user)
            super(UserProfile, self).save(*args, **kwargs)    

    def __str__(self):
        return self.name


class UserProject(models.Model):
    project = models.ForeignKey(UserProfile, related_name="profile")
    title = models.CharField(max_length=200)
    image = models.ImageField (upload_to="project_images/",null=True,blank=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title


