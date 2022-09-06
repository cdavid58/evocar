from django.shortcuts import render
from .models import Course
from home.models import Information as information
from trainers.models import Trainer
import random

def List_Courses(request):
	course = Course.objects.all()
	_data = [
		{
			'pk':i.pk,
			'title':i.title,
			'img':i.img_course.url,
			'price':i.price,
			'trainer':Trainer.objects.get(pk = i.trainer.pk),
			'description':i.description
		}
		for i in course
	]
	_info = information.objects.last()
	return render(request,'courses.html',{'course':_data,'info':_info})


def Course_Details(request,pk):
	course = Course.objects.get(pk = pk)
	_info = information.objects.last()
	return render(request,'course-details.html', {'course':course,'seats':random.randint(0,30),'info':_info})
