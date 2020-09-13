from django.urls import path
from . import views
from .views import (PostCreateView)

urlpatterns = [
    path('', PostCreateView.as_view(), name='blog-home'),
     path('Cv/',views.Cv,name='cv_detail')



]