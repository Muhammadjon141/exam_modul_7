from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Get_info
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import (Course, Tasks, Lesson, Modules)
from .serializers import (CategorySerializer, StudentGroupSerializer, GroupSerializer, TasksSerializer, LessonSerializer, ModulesSerializer,
                          CourseSerializer, TeacherSerializer, StudentSerializer, MessageSerializer)

class CategoryApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Category')
    serializer_class = CategorySerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class StudentGroupApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('StudentGroup')
    serializer_class = StudentGroupSerializer 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]   

class GroupApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Group')
    serializer_class = GroupSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class TasksApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Tasks')
    serializer_class = TasksSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def active_tasks(self, request):
        active = Tasks.objects.filter(status='pb')
        serializer = self.get_serializer(active, many=True)
        return Response(serializer.data)
    
class LessonApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Lesson')
    serializer_class = LessonSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def active_lesson(self, request):
        active = Lesson.objects.filter(status='pb')
        serializer = self.get_serializer(active, many=True)
        return Response(serializer.data) 

class ModulesApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Modules')
    serializer_class = ModulesSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def active_modules(self, request):
        active = Modules.objects.filter(status='pb')
        serializer = self.get_serializer(active, many=True)
        return Response(serializer.data)
    

class CourseApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Course')
    serializer_class = CourseSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def active_courses(self, request):
        active = Course.objects.filter(status='pb')
        serializer = self.get_serializer(active, many=True)
        return Response(serializer.data)

class TeacherApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Teacher')
    serializer_class = TeacherSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class StudentApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Student')
    serializer_class = StudentSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class MessageApiWeb(ModelViewSet):
    queryset = Get_info.get_queryset('Message')
    serializer_class = MessageSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]