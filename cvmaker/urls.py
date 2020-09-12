from django.urls import path
from . import views
from .views import (PostCreateView,PostListView)

urlpatterns = [
    path('', PostCreateView.as_view(), name='blog-home'),
     path('Cv/',PostListView.as_view(),name='cv_detail')



]