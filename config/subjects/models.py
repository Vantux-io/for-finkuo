from django.db import models
from departments.models import Department
from django.utils import timezone 


class Subject(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()
    credit_hours = models.IntegerField()
    grade_level = models.IntegerField(choices=[(i, f'Grade {i}') for i in range(9, 13)])
    prerequisites = models.ManyToManyField('self', blank=True)
    date_created = models.DateTimeField(default=timezone.now)  

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['department', 'grade_level']),
        ]

    def __str__(self):
        return self.name
