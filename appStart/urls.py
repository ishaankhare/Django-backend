from django.urls import path
from . import views

urlpatterns = [
    path('liveliness/', views.liveliness),
    path('readiness/', views.readiness),
]
