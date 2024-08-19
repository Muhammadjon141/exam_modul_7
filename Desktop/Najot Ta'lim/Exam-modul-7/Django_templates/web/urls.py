from django.urls import path
from .views import (Index_View, Login_View, Register_View, Log_OutView, Team_View, Testimonial_View, Service_View, Offer_View,
                    Feature_View, FAQ_View, Contact_View, Blog_View, Course_View, Error_View, CoursedetailView)

urlpatterns = [
    path('', Index_View.as_view(), name='index'),
    path('login/', Login_View.as_view(), name='login'),
    path('register/', Register_View.as_view(), name='register'),
    path('logout/', Log_OutView.as_view(), name='logout'),
    path('team/', Team_View.as_view(), name='team'),
    path('testimonial/', Testimonial_View.as_view(), name='testimonial'),
    path('service/', Service_View.as_view(), name='service'),
    path('offer/', Offer_View.as_view(), name='offer'),
    path('feature/', Feature_View.as_view(), name='feature'),
    path('faq/', FAQ_View.as_view(), name='faq'),
    path('contact/', Contact_View.as_view(), name='contact'),
    path('blog/', Blog_View.as_view(), name='blog'),
    path('course/', Course_View.as_view(), name='course'),
    path('error/', Error_View.as_view(), name='error'),
    path('course-detail/<int:id>', CoursedetailView.as_view(), name='course-detail'),
]