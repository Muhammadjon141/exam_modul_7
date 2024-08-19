from .views import (CategoryApiWeb, StudentGroupApiWeb, GroupApiWeb, TasksApiWeb, LessonApiWeb, ModulesApiWeb, 
                    CourseApiWeb, TeacherApiWeb, StudentApiWeb, MessageApiWeb)
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'category', CategoryApiWeb, basename='category'),
router.register(r'student-group', StudentGroupApiWeb, basename='student-group'),
router.register(r'tasks', TasksApiWeb, basename='tasks'),
router.register(r'lesson', LessonApiWeb, basename='lesson'),
router.register(r'group', GroupApiWeb, basename='group'),
router.register(r'modules', ModulesApiWeb, basename='modules'),
router.register(r'course', CourseApiWeb, basename='course'),
router.register(r'teacher', TeacherApiWeb, basename='teacher'),
router.register(r'student', StudentApiWeb, basename='student'),
router.register(r'message', MessageApiWeb, basename='message'),

urlpatterns = [
    path('', include(router.urls)),
]
