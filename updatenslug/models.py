from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class DemoFormm(models.Model):
	name = models.CharField(max_length=120)
	msg = models.TextField(unique=True)
	img = models.ImageField(upload_to = 'images/' , null=True, blank = True)
	slug = models.CharField(unique=True, max_length=100)
	tags = TaggableManager()

	class Meta:
		ordering = ('-id',)
