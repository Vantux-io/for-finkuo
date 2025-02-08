from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_teacher, name='add_teacher'),
    path('list/', views.list_teachers, name='list_teachers'),
]