from django.shortcuts import render
from .models import cv
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView,ListView

def home(request):
	return render(request,'cvmaker/home.html')


def Cv(request):
	context = {
		'cvs': cv.objects.last()
	}
	return render(request,'cvmaker/srt-resume.html',context)




class PostCreateView(LoginRequiredMixin, CreateView):
	model = cv
	fields = ['fullname', 'job_title','profile', 'skill_1','skill_2', 'skill_3','Technicale', 'education']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)