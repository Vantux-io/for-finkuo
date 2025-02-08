from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_department, name='add_department'),
    path('list/', views.list_departments, name='list_departments'),
]