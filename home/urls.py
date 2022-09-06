from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Home,name="Home"),
	url(r'^Contact/$',Contact,name="Contact"),
	url(r'^About/$',About,name="About"),
]