from django.shortcuts import render
from rest_framework import serializers , views , response , status
from .models import *
from django.contrib.auth.models import User
from django.http import Http404
# Create your views here.


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password')

class ProfessorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Professor
        fields = ('id','user')
        depth = 1

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Professor
        fields = ('id','user')
        depth = 1

class UserViewsets(views.APIView):
    
    def get_object(self, pk):
        try :
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404
    def get(self , request , pk , format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user,many=False,context={'request':request})
        return response.Response(serializer.data)

class ProjectViewsets(views.APIView):
    @classmethod
    def get_extra_actions(cls):
        return []

    basename = 'project-view'
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProfessorSerializer(projects,many=True,context={'request':request})
        return response.Response(serializer.data)
    
    def post(self, request, format=None):
        projects = Project.objects.get(data=request.data)
        serializer = ProjectSerializer(projects,many=True,context={'request':request})
        if serializer.is_valid():
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailViewsets(views.APIView):
    @classmethod
    def get_extra_actions(cls):
        return []
            
    basename = 'project-detail-view'    
    def get_object(self , pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404
    def get(self , request , pk , format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project,many=False,context={'request':request})
        return response.Response(serializer.data)

    def put(self , request , pk , format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project,many=False,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk , format=None):
        project = self.get_object(pk)
        project.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)        

class ProfessorViewsets(views.APIView):
    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors,many=True,context={'request':request})
        return response.Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            NewProf = User.objects.create_user(username=request.data['user']['username'],email=request.data['user']['email'],password=request.data['user']['password'])
            NewProf.save()
            Prof = Professor(user=NewProf)
            Prof.save()
            return response.Response(serializer.data , status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ProfessorDetailViewsets(views.APIView):
    @classmethod
    def get_extra_actions(cls):
        return []

    def get_object(self, pk):
        try:
            return Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            raise Http404

    def get(self, request , pk , format=None):
        professors = self.get_object(pk)
        serializer = ProfessorSerializer(professors,many=False,context={'request':request})
        return response.Response(serializer.data)
    
    def put(self, request , pk , format=None):
        professors = self.get_object(pk)
        serializer = ProfessorSerializer(professors,many=False,context={'request':request})   
        if serializer.is_valid():
            serializer.save()       
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk , format=None):
        professors = self.get_object(pk)
        professors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentViewsets(views.APIView):
    @classmethod
    def get_extra_actions(cls):
        return []
    basename = 'student-view'
    def get(self , request , format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True,context={'request':request})
        return response.Response(serializer.data)

    
    def post(self , request , format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetailViewsets(views.APIView):
    basename = 'student-detail-view'
    def get_object(self , pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self , request , pk , format=None):

        student = self.get_object(pk)
        serializer = StudentSerializer(student,many=False,context={'request':request})
        return response.Response(serializer.data)

    def put(self , request , pk , format=None):

        student = self.get_object(pk)
        serializer = StudentSerializer(student,many=False,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk , format=None):

        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

