from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),  # Добавим маршрут для логина
]
