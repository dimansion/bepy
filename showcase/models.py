from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from dashboard.models import UserProfile


class UserProject(models.Model):
    project = models.ForeignKey(UserProfile, related_name="profile")
    title = models.CharField(max_length=200)
    image = models.ImageField (upload_to="project_images/",null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    url = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(UserProject, self).save(*args, **kwargs)   

    def __str__(self):
        return self.title

