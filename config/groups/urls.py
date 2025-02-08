from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_group, name='add_group'),
    path('list/', views.list_groups, name='list_groups'),
]