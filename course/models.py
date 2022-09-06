from django.db import models
from trainers.models import Trainer


class Course(models.Model):
	title = models.CharField(max_length=70)
	price = models.CharField(max_length = 10)
	description = models.TextField()
	trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)
	img_course = models.ImageField(upload_to = 'Course',default = "")

	def __str__(self):
		return self.title


