from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse





class cv(models.Model):
	fullname=models.CharField(max_length=100)
	job_title=models.CharField(max_length=100)
	profile=models.TextField()
	skill_1=models.CharField(max_length=100)
	skill_2=models.CharField(max_length=100)
	skill_3=models.CharField(max_length=100)
	Technicale=models.TextField()
	education=models.TextField()
	author = models.ForeignKey(User , on_delete = models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def get_absolute_url(self):
		return reverse('cv_detail')
