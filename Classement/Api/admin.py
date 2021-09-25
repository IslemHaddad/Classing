from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = 'DataBase'

admin.site.register(Wilaya)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Departement)
admin.site.register(Speciality)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Professor)
