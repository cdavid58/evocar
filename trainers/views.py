from django.shortcuts import render
from .models import Trainer,Information
from home.models import Information as information

def Profile_Trainers(request):
	trainer = Trainer.objects.all()
	info = Information.objects.last()
	_info = information.objects.last()
	return render(request,'trainers.html',{'trainer':trainer,'info_':info,'info':_info})
