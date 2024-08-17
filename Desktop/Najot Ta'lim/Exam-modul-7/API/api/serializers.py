from rest_framework import serializers
from .models import StudentGroup, Group, Student, Tasks, Lesson, Modules, Course, Teacher, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'status']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name', 'last_name', 'image', 'username']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','first_name', 'last_name', 'image', 'username']
        
class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False,read_only=True)
    category = CategorySerializer(many=False,read_only=True)
    class Meta:
        model = Course
        fields = ['title', 'description', 'price', 'image', 'teacher', 'category', 'status']

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = ['name', 'description', 'course', 'status']
        
class LessonSerializer(serializers.ModelSerializer):
    modules = ModulesSerializer(many=False, read_only=True)
    class Meta:
        model = Lesson
        fields = ['name', 'description', 'modules', 'status']

class TasksSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=False, read_only=True)
    class Meta:
        model = Tasks
        fields = ['name', 'file', 'lesson', 'status']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'teacher', 'course', 'status']

class StudentGroupSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=True, read_only=True)
    student = StudentSerializer(many=True, read_only=True)
    class Meta:
        model = StudentGroup
        fields = ['group', 'student', 'status']