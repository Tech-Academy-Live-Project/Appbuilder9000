from django.urls import path
from . import views

urlpatterns = [
    path('', views.ja3_home, name='ja3_home'),
]