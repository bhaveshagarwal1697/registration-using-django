from django.db import models

# Create your models here.

class Profile(models.Model):
	# to map with database we use models
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	experience	= models.DecimalField(decimal_places=1, max_digits=1000000)
	summary		= models.TextField(default='Add summary')