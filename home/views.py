from django.shortcuts import render
from .models import Information
from course.models import Course
from trainers.models import Trainer


def Home(request):
	info = Information.objects.last()
	import sqlite3
	con = sqlite3.connect('db.sqlite3')
	c = con.cursor()
	c.execute("""
		SELECT DISTINCT * FROM course_course desc limit 3
	""")
	data = c.fetchall()
	print(data)
	_data = [
		{
			'pk':i[0],
			'title':i[1],
			'img':"http://localhost:8000/media/"+i[5],
			'price':i[2],
			'trainer':Trainer.objects.get(pk = i[4]),
			'description':i[3]
		}
		for i in data
	]
	n_trainer = len(Trainer.objects.all())
	return render(request,'index.html',{'info':info,'data':_data,'n_trainer':n_trainer})


def Contact(request):
	info = Information.objects.last()
	return render(request,'contact.html',{'info':info})

def About(request):
	info = Information.objects.last()
	n_trainer = len(Trainer.objects.all())
	return render(request,'about.html',{'info':info,'n_trainer':n_trainer})
