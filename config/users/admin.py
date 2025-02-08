from django.contrib import admin
from .models import CustomUser, ActivityLog
from departments.models import Department
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from subjects.models import Subject


admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(ActivityLog)

