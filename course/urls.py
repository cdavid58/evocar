from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Courses/$',List_Courses,name="List_Courses"),
	url(r'^Course_Details/(\d+)/$',Course_Details,name="Course_Details"),
]