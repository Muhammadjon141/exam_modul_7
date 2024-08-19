from .views import (CategoryApiWeb, StudentGroupApiWeb, GroupApiWeb, TasksApiWeb, LessonApiWeb, ModulesApiWeb, 
                    CourseApiWeb, TeacherApiWeb, StudentApiWeb, MessageApiWeb)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="API documentation for my project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]