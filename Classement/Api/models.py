from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Wilaya(models.Model):
    name = models.CharField(max_length=50,null=True)
    code_postal = models.IntegerField()
    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=50)
    wilaya = models.ForeignKey(Wilaya,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Universities'

class Faculty(models.Model):
    code = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=10,null=True)
    university = models.ForeignKey(University,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name    
    class Meta:
        verbose_name_plural = 'Faculties'

class Departement(models.Model):
    name = models.CharField(max_length=20,null=True)
    faculty = models.ManyToManyField(Faculty)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name  

class Speciality(models.Model):
    name = models.CharField(max_length=10,null=True)
    label = models.CharField(max_length=50,null=True)
    Departement = models.ForeignKey(Departement,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Specialities'


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    codex = models.IntegerField(primary_key=True)
    first_semester = models.FloatField()
    def __str__(self):
        return self.name

class Professor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Project(models.Model):
    title = models.CharField(max_length=20,null=True)
    label = models.CharField(max_length=50,null=True)
    speciality = models.ForeignKey(Speciality,on_delete=models.CASCADE)
    Student = models.ForeignKey(Student,on_delete=models.PROTECT,null=True)
    professor = models.ForeignKey(Professor,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
