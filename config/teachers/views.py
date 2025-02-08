from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_teachers')  # Redirect to dashboard after saving
    else:
        form = TeacherForm()
    return render(request, 'teachers/form.html', {'form': form})


def list_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/list.html', {'teachers': teachers})

