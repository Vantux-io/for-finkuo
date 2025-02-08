from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from subjects.models import Subject



class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    


    groups = models.ManyToManyField(
        'auth.Group',
        related_name="customuser_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="customuser_permissions",
        blank=True,
    )

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'



class ActivityLog(models.Model):
    EVENT_TYPES = [
        ('student_enrolled', 'New Student Enrolled'),
        ('assignment_completed', 'Assignment Completed'),
        ('schedule_added', 'New Schedule Added'),
    ]

    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    description = models.TextField()
    timestamp = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.get_event_type_display()} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True) 
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name='assignments')

    teacher = models.ForeignKey("teachers.Teacher", on_delete=models.SET_NULL, null=True, related_name='assignments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.student}"

class Schedule(models.Model):       
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey("teachers.Teacher", on_delete=models.CASCADE)
    students = models.ManyToManyField("students.Student", related_name='schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"
