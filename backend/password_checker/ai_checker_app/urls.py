from django.urls import path
from . import views

urlpatterns = [
    path('check-password/', views.check_password, name='check-password'),
]