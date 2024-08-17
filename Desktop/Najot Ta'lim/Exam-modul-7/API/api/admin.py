from django.contrib import admin
from .models import StudentGroup, Group, Student, Tasks, Lesson, Modules, Course, Teacher, Category

admin.site.register([StudentGroup, Group, Student, Tasks, Lesson, Modules, Course, Teacher, Category])