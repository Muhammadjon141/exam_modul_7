from django.db import models
from api.models import Student, Group
from django.utils import timezone
from django.apps import apps

class Payment(models.Model):
    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.amount}{self.student}{self.group}"

    class Meta:
        ordering = ['-payment_date']
        

class Get_info:
    @staticmethod
    def get_queryset(model_name):
        try:
            # Dinamik ravishda modelni olish
            model = apps.get_model('payment', model_name)
            
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
            model = apps.get_model('payment', model_name)
            
            if model:
                # Ushbu modelning barcha obyektlarini olish
                query_set = model.objects.get(id=id)
                return query_set
            else:
                return None
        except LookupError:
            return None