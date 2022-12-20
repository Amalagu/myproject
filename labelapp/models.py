from django.db import models
from datetime import date
# Create your models here.

class Image(models.Model):
	title = models.CharField(max_length=150, null=False)
	description=models.CharField(max_length=300)
	owner = models.CharField(max_length=50, default="Manager")
	upload_time = models.DateField(default = date.today)
	annotated = models.BooleanField(default=False)
	source = models.CharField(max_length =50, default = "Unknown Source")
	modified = models.DateField(default = date.today)
	picture = models.ImageField(upload_to='pictures', null=True, blank=True)
	
	"""def save(self, *args, **kwargs):
		self.modified = models.DateField(default = date.today)
		super(Image, self).save(*args, **kwargs)"""
