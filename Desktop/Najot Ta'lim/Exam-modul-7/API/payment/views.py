from django.shortcuts import render
from .models import Get_info
from .serializers import PaymentSerializer
from rest_framework.viewsets import ModelViewSet

class PaymentViewsSet(ModelViewSet):
    queryset = Get_info.get_queryset('Payment')
    serializer_class = PaymentSerializer
    # authentication_classes = ['IsAuthenticated']