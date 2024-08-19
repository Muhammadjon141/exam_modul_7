from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import (StudentGroup, Group, Student, Tasks, Lesson, Modules,
                     Course, Teacher, Category, Message)

@admin.register(Teacher)
class Teacher_Admin(ImportExportModelAdmin):
    readonly_fields = ['status_st_tch', ]
    list_display = ['first_name', 'last_name', 'status_st_tch']
    list_display_links = ['first_name', 'last_name', 'status_st_tch']
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    
@admin.register(Student)
class Student_Admin(ImportExportModelAdmin):
    readonly_fields = ['status_st_tch', ]
    list_display = ['first_name', 'last_name', 'status_st_tch']
    list_display_links = ['first_name', 'last_name', 'status_st_tch']
    search_fields = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    
@admin.register(StudentGroup)
class StudentGroup_Admin(ImportExportModelAdmin):
    list_display = ['group', 'student', 'status']
    list_display_links = ['group', 'student', 'status']
    search_fields = ['group',]
    ordering = ['id']

@admin.register(Group)
class Group_Admin(ImportExportModelAdmin):
    list_display = ['name', 'teacher', 'course', 'status']
    list_display_links = ['name', 'teacher', 'course', 'status']
    search_fields = ['name',]
    ordering = ['id']    

@admin.register(Tasks)
class Tasks_Admin(ImportExportModelAdmin):
    list_display = ['name', 'file', 'lesson', 'status']
    list_display_links = ['name', 'file', 'lesson', 'status']
    search_fields = ['name', ]
    ordering = ['id']

@admin.register(Lesson)
class Lesson_Admin(ImportExportModelAdmin):
    list_display = ['name', 'description', 'modules', 'status']
    list_display_links = ['name', 'description', 'modules', 'status']
    search_fields = ['name',]
    ordering = ['id']

@admin.register(Modules)
class Modules_Admin(ImportExportModelAdmin):
    list_display = ['name', 'description', 'course', 'status']
    list_display_links = ['name', 'description', 'course', 'status']
    search_fields = ['name', ]
    ordering = ['id']

@admin.register(Course)
class Course_Admin(ImportExportModelAdmin):
    list_display = ['title', 'description', 'price', 'image', 'teacher', 'category', 'status']
    list_display_links = ['title', 'description', 'price', 'image', 'teacher', 'category', 'status']
    search_fields = ['title', ]
    ordering = ['id']
    
@admin.register(Category)
class Category_Admin(ImportExportModelAdmin):
    list_display = ['name', 'status']
    list_display_links = ['name', 'status']
    search_fields = ['name', ]
    ordering = ['id']
    
@admin.register(Message)
class Message_Admin(ImportExportModelAdmin):
    list_display = ['first_name', 'username']
    list_display_links = ['first_name', 'username']
    search_fields = ['first_name', ]
    ordering = ['id']