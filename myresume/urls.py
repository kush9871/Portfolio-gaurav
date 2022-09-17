from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('service/',views.service,name='service'),
  path('skill/',views.skill,name='skill'),
  path('project/',views.projects,name='projects'),
  path('qualification/',views.qualification,name='qualification'),
]