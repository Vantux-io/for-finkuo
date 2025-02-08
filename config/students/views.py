from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')  # Redirect to dashboard after saving
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form})


def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

