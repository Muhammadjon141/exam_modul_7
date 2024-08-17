from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Get_info
from rest_framework.decorators import action
from rest_framework import status
from .serializers import (CategorySerializer, StudentGroupSerializer, GroupSerializer, TasksSerializer, LessonSerializer, ModulesSerializer,
                          CourseSerializer, TeacherSerializer, StudentSerializer)

class CategoryApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Category')
    serializer_class = CategorySerializer    

class StudentGroupApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('StudentGroup')
    serializer_class = StudentGroupSerializer    

class GroupApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Group')
    serializer_class = GroupSerializer    
    
class TasksApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Tasks')
    serializer_class = TasksSerializer    
    
class LessonApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Lesson')
    serializer_class = LessonSerializer    

class ModulesApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Modules')
    serializer_class = ModulesSerializer    

class CourseApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Course')
    serializer_class = CourseSerializer    

class TeacherApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Teacher')
    serializer_class = TeacherSerializer    

class StudentApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Student')
    serializer_class = StudentSerializer    