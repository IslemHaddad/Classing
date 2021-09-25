from django.contrib import admin
from django.urls import path , include
from rest_framework import routers
from .views import *

urlpatterns = [

    path(r'professor/',ProfessorViewsets.as_view()),
    path(r'professor/<int:pk>',ProfessorDetailViewsets.as_view()),
    path(r'student/',StudentViewsets.as_view()),
    path(r'student/<int:pk>',StudentDetailViewsets.as_view()),
    path(r'project/',ProfessorViewsets.as_view()),
    path(r'project/<int:pk>',ProjectDetailViewsets.as_view()),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]