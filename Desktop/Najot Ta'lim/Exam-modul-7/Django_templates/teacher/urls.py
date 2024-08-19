from django.urls import path
from .views import (Index_View, Login_View, Register_View, Log_OutView, Team_View, Testimonial_View, Service_View, Offer_View,
                    Feature_View, FAQ_View, Contact_View, Blog_View, Course_View, Error_View, CourseDetailView)

urlpatterns = [
    path('', Index_View.as_view(), name='index-t'),
    path('login/', Login_View.as_view(), name='login-t'),
    path('register/', Register_View.as_view(), name='register-t'),
    path('logout/', Log_OutView.as_view(), name='logout-t'),
    path('team/', Team_View.as_view(), name='team-t'),
    path('testimonial/', Testimonial_View.as_view(), name='testimonial-t'),
    path('service/', Service_View.as_view(), name='service-t'),
    path('offer/', Offer_View.as_view(), name='offer-t'),
    path('feature/', Feature_View.as_view(), name='feature-t'),
    path('faq/', FAQ_View.as_view(), name='faq-t'),
    path('contact/', Contact_View.as_view(), name='contact-t'),
    path('blog/', Blog_View.as_view(), name='blog-t'),
    path('course/', Course_View.as_view(), name='course-t'),
    path('error/', Error_View.as_view(), name='error-t'),
    path('course-detail/<slug:slug>/', CourseDetailView.as_view(), name='course-detail-t'),
]