from django.db import models

class Trainer(models.Model):
	name = models.CharField(max_length = 35)
	profession = models.CharField(max_length = 100)
	description = models.TextField()
	img_profile = models.ImageField(upload_to = "Trainer")

	def __str__(self):
		return self.name


class Information(models.Model):
	title = models.CharField(max_length = 50)
	message = models.CharField(max_length= 150)
	
