from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Page(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Page, self).save(*args, **kwargs)    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Content(models.Model):
	lesson = models.ForeignKey(Page, related_name="page")
	name = models.CharField(max_length=128, unique=True)
	link = models.URLField(null=True, blank=True)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Content, self).save(*args, **kwargs)   

	def __str__(self):
		return self.name

