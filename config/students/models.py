from django.db import models 
from groups.models import Group
from django.utils import timezone 
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    grade = models.IntegerField(choices=[(i, f'Grade {i}') for i in range(9, 13)])
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    parent_email = models.EmailField()
    date_created = models.DateTimeField(default=timezone.now)  


    class Meta:
        ordering = ['user__last_name']
        indexes = [
            models.Index(fields=['grade', 'group']),
        ]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
