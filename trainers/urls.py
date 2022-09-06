from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Profile_Trainers/$',Profile_Trainers,name="Profile_Trainers"),
]