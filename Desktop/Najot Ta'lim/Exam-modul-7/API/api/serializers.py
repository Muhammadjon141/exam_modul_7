from rest_framework import serializers
from .models import StudentGroup, Group, Student, Tasks, Lesson, Modules, Course, Teacher, Category, Message

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'status', 'created_at']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'image', 'email', 'username', 'password', 'phone_number', 'status', 'status_st_tch']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'image', 'email', 'username', 'password', 'phone_number', 'status', 'status_st_tch']
        
class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False,read_only=True)
    category = CategorySerializer(many=False,read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'slug', 'description', 'price', 'image', 'teacher', 'category', 'status', 'created_at']

class ModulesSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=False,read_only=True)
    class Meta:
        model = Modules
        fields = ['id', 'name', 'slug', 'description', 'course', 'status', 'created_at']
        
class LessonSerializer(serializers.ModelSerializer):
    modules = ModulesSerializer(many=False, read_only=True)
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'slug', 'description', 'modules', 'status', 'created_at']

class TasksSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=False, read_only=True)
    class Meta:
        model = Tasks
        fields = ['id', 'name', 'slug', 'file', 'lesson', 'status', 'created_at']

class GroupSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False,read_only=True)
    course = CourseSerializer(many=False,read_only=True)
    class Meta:
        model = Group
        fields = ['id', 'name', 'slug', 'teacher', 'course', 'status', 'created_at']

class StudentGroupSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=False, read_only=True)
    student = StudentSerializer(many=False, read_only=True)
    class Meta:
        model = StudentGroup
        fields = ['id', 'group', 'student', 'status']
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'username', 'message', 'created_at']