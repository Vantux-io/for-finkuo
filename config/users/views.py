from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import ProfileUpdateForm
from students.models import Student
from teachers.models import Teacher
from groups.models import Group
from subjects.models import Subject
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.timezone import now
from datetime import timedelta
from .models import ActivityLog
from datetime import datetime
from django.db.models import Count


 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
  
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in successfully!')
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')





#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# zb qgan main function: 

@login_required
def dashboard(request):
    today = now()
    first_day_of_current_month = today.replace(day=1)
    first_day_of_last_month = (first_day_of_current_month - timedelta(days=1)).replace(day=1)

    total_students = Student.objects.count()
    students_last_month = Student.objects.filter(date_created__lt=first_day_of_current_month, date_created__gte=first_day_of_last_month).count()
 
    if students_last_month > 0:   
        student_growth = ((total_students - students_last_month) / students_last_month) * 100     
    else:
        student_growth = 0         



    total_teachers = Teacher.objects.count()
    total_groups = Group.objects.count()
    total_subjects = Subject.objects.count()

    current_year = datetime.now().year
    last_year = current_year - 1

    current_month = now().month
    
    enrollments_current = [
        Student.objects.filter(date_created__year=current_year, date_created__month=month).count()
        for month in range(1, current_month + 1)
    ]
    enrollments_last = [
        Student.objects.filter(date_created__year=last_year, date_created__month=month).count()
        for month in range(1, 13)
    ]
 
    subject_data = list(
        Subject.objects.annotate(student_count=Count('group__student', distinct=True))
        .values_list('name', 'student_count')
    )

    subject_labels, subject_distribution = zip(*subject_data) if subject_data else ([], [])

    one_month_ago = now() - timedelta(days=30)

    new_teachers = Teacher.objects.filter(date_created__gte=one_month_ago).count()
    new_groups = Group.objects.filter(date_created__gte=one_month_ago).count()
    new_subjects = Subject.objects.filter(date_created__gte=one_month_ago).count()

    recent_activities = ActivityLog.objects.all()[:5]

    context = {
        'total_students': total_students,
        'student_growth':  student_growth,
        'total_teachers': total_teachers,
        'new_teachers': new_teachers if new_teachers > 0 else "No change",
        'total_groups': total_groups,
        'new_groups': new_groups if new_groups > 0 else "No change",
        'total_subjects': total_subjects,
        'new_subjects': new_subjects if new_subjects > 0 else "No change",
        'current_year': current_year,
        'last_year': last_year,
        'enrollments_current': enrollments_current,
        'enrollments_last': enrollments_last,
        'subject_labels': list(subject_labels),
        'subject_distribution': list(subject_distribution),
        'recent_activities': recent_activities,
    }

    return render(request, 'dashboard.html', context)

 

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------




@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('dashboard')
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'profile-update.html', context)

# Logout View
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')  # Redirect to the login page after logout