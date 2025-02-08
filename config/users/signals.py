from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Assignment, Schedule, ActivityLog
from students.models import Student

@receiver(post_save, sender=Student)
def log_student_enrollment(sender, instance, created, **kwargs):
    if created:
        ActivityLog.objects.create(
            event_type='student_enrolled',
            description=f"{instance.user.first_name} {instance.user.last_name} joined {instance.group}."
        )

@receiver(post_save, sender=Assignment)
def log_assignment_completion(sender, instance, created, **kwargs):
    if not created:  
        ActivityLog.objects.create(
            event_type='assignment_completed',
            description=f"{instance.subject} - {instance.student.user.first_name} {instance.student.user.last_name} submitted their assignment."
        )

@receiver(post_save, sender=Schedule)
def log_new_schedule(sender, instance, created, **kwargs):
    if created:
        student_names = ', '.join([s.user.first_name for s in instance.students.all()])
        ActivityLog.objects.create(
            event_type='schedule_added',
            description=f"{instance.subject} class scheduled for {student_names}."
        )

