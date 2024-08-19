from .models import Payment
from rest_framework import serializers
from api.serializers import StudentSerializer, GroupSerializer

class PaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False, read_only=True)
    group = GroupSerializer(many=False, read_only=True)
    class Meta:
        model = Payment
        fields = ['id', 'student', 'group', 'amount', 'payment_date', 'status', 'transaction_id']