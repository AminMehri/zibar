from django.contrib import admin
from django.urls import path, include
from zibar import views

urlpatterns = [
    path('ContactUs/', views.ContactUs.as_view(), name="contact_us"),    
]
