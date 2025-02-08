from django.db import models 
from departments.models import Department
from subjects.models import Subject
from django.utils import timezone 
from django.contrib.auth import get_user_model

User = get_user_model()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    qualification = models.CharField(max_length=255)
    join_date = models.DateField()
    employment_type = models.CharField(max_length=10, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('contract', 'Contract')])
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)  


    class Meta:
        ordering = ['user__last_name']
        indexes = [
            models.Index(fields=['department', 'join_date']),
        ]

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
