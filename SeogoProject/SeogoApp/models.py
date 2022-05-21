from django.db import models

# Create your models here.
class contact_info(models.Model):
	message = models.TextField(max_length = 1000)
	name = models.CharField(max_length= 300)
	email = models.CharField(max_length= 300)
	subject = models.CharField(max_length= 500)


	def __str__(self):
		return self.name