from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from dashboard.models import UserProfile


class UserProject(models.Model):
    project = models.ForeignKey(UserProfile, related_name="profile")
    title = models.CharField(max_length=200)
    image = models.ImageField (upload_to="project_images/",null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    url = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = UserProject.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=UserProject)        

