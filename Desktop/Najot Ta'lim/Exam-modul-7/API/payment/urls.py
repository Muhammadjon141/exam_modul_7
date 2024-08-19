from .views import PaymentViewsSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'payment', PaymentViewsSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]