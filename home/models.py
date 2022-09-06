from django.db import models

class Information(models.Model):
	company_name = models.CharField(max_length=60)
	company_slogan = models.CharField(max_length = 150)
	company_logo = models.ImageField(upload_to = "Logo")
	text1_banner = models.CharField(max_length = 250)
	text2_banner = models.CharField(max_length= 200)
	address_1 = models.CharField(max_length = 150,default="")
	address_2 = models.CharField(max_length = 150, null=True,blank=True)
	country = models.CharField(max_length = 50,default="")
	phone = models.CharField(max_length = 25,default="")
	email = models.EmailField(default="")
	title_about = models.CharField(max_length = 100,default = "")
	about = models.TextField(default = "")
	img_about = models.ImageField(upload_to = "About",default = "",blank = True, null = True)




	