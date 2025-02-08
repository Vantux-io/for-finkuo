from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_subject, name='add_subject'),
    path('list/', views.list_subjects, name='list_subjects'),
]