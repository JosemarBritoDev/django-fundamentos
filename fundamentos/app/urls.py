from django.contrib import admin
from django.urls import path, include
from .views import horario_atual  # Import the function from views

urlpatterns = [
path('horario_atual', horario_atual)
]