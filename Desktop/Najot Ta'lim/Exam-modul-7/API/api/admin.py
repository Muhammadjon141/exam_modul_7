from django.contrib import admin
from .models import StudentGroup, Group, Student, Tasks, Lesson, Modules, Course, Teacher, Category

@admin.register(Teacher)
class Teacher_Admin(admin.ModelAdmin):
    readonly_fields = ['status_st_tch', ]
    list_display = ['first_name', 'last_name', 'status_st_tch']
    list_display_links = ['first_name', 'last_name', 'status_st_tch']
    
    

@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    readonly_fields = ['status_st_tch', ]
    list_display = ['first_name', 'last_name', 'status_st_tch']
    list_display_links = ['first_name', 'last_name', 'status_st_tch']
    
admin.site.register([StudentGroup, Group, Tasks, Lesson, Modules, Course, Category])