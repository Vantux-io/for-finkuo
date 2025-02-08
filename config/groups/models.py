from django.db import models
from teachers.models import Teacher
from subjects.models import Subject
from django.utils import timezone 


class Group(models.Model):
    name = models.CharField(max_length=100)
    grade_level = models.IntegerField(choices=[(i, f'Grade {i}') for i in range(9, 13)])
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    schedule = models.CharField(max_length=20, choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')])
    academic_year = models.CharField(max_length=10)
    max_students = models.IntegerField()
    subjects = models.ManyToManyField(Subject)
    date_created = models.DateTimeField(default=timezone.now)  


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['academic_year', 'grade_level']),
        ]

    def __str__(self):
        return self.name
