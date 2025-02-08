from django.db import models
from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='head_of_department')
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
    
    def full_info(self):
        return f'{self.name} - {self.head} ({self.contact_email})'
