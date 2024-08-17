from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser

class Status(models.TextChoices):
    draft = 'df', 'draft'
    publish = 'pb', 'publish'


class Status_st_tch(models.TextChoices):
    student = 'st', 'student'
    teacher = 'tch', 'teacher'

class User(AbstractUser):
    image = models.ImageField(upload_to='users/')
    phone_number = models.CharField(max_length=15, unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # related_name o'zgartirildi
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_permission_set',  # related_name o'zgartirildi
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateField(auto_now_add=True)
    
class Teacher(User):
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    status_st_tch = models.CharField(max_length=4, choices=Status_st_tch.choices, default=Status_st_tch.teacher, editable=False)
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = 'Teachers'
        
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='courses/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Modules(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    modules = models.ForeignKey(Modules, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Tasks(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='file_tasks/')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)

class Student(User):
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    status_st_tch = models.CharField(max_length=4, choices=Status_st_tch.choices, default=Status_st_tch.student, editable=False)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        
class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
class StudentGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Get_info:
    @staticmethod
    def get_queryset(model_name):
        try:
            # Dinamik ravishda modelni olish
            model = apps.get_model('api', model_name)
            
            if model:
                # Ushbu modelning barcha obyektlarini olish
                query_set = model.objects.all()
                return query_set
            else:
                return None
        except LookupError:
            return None
        
    @staticmethod
    def get_object(model_name, id):
        try:
            # Dinamik ravishda modelni olish
            model = apps.get_model('api', model_name)
            
            if model:
                # Ushbu modelning barcha obyektlarini olish
                query_set = model.objects.get(id=id)
                return query_set
            else:
                return None
        except LookupError:
            return None