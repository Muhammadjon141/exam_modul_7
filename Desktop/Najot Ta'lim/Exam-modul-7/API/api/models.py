from django.db import models
from django.apps import apps
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class Status(models.TextChoices):
    draft = 'df', 'draft'
    publish = 'pb', 'publish'


class Status_st_tch(models.TextChoices):
    student = 'st', 'student'
    teacher = 'tch', 'teacher'

class User(AbstractUser):
    slug = models.SlugField(unique=True, null=True, blank=True)
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
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['id',]
        indexes = [
            models.Index(fields=['id'])
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    
class Teacher(User):
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    status_st_tch = models.CharField(max_length=4, choices=Status_st_tch.choices, default=Status_st_tch.teacher, editable=False)
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = 'Teachers'
        ordering = ['first_name',]
        indexes = [
            models.Index(fields=['status'])
        ]
        
class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='courses/')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id', ]
        indexes = [
            models.Index(fields=['id'])
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    
class Modules(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id',]
        indexes = [
            models.Index(fields=['id'])
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Modules, self).save(*args, **kwargs)

    
class Lesson(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    modules = models.ForeignKey(Modules, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id',]
        indexes = [
            models.Index(fields=['id'])
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Lesson, self).save(*args, **kwargs)

    
class Tasks(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    file = models.FileField(upload_to='file_tasks/')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id',]
        indexes = [
            models.Index(fields=['id'])
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tasks, self).save(*args, **kwargs)

class Student(User):
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    status_st_tch = models.CharField(max_length=4, choices=Status_st_tch.choices, default=Status_st_tch.student, editable=False)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['first_name',]
        indexes = [
            models.Index(fields=['status'])
        ]
        
class Group(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id',]
        indexes = [
            models.Index(fields=['id'])
        ]
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Group, self).save(*args, **kwargs)

    
class StudentGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.publish)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['id',]
        indexes = [
            models.Index(fields=['id'])
        ]
    
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
        
class Message(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save_phone_number(self, *args, **kwargs):
        try:
            if Student.objects.get(phone_number=self.phone_name):
                super().save(*args, **kwargs)
        except:
            return 'failed phone_number'
    
    def save_username(self, *args, **kwargs):
        try:
            if Student.objects.get(username=self.username):
                super().save(*args, **kwargs)
        except:
            return 'failed username'