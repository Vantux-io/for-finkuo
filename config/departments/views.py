from django.shortcuts import render, redirect
from .forms import DepartmentForm
from .models import Department


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = DepartmentForm()
    return render(request, 'departments/form.html', {'form': form})


def list_departments(request):
    departments = Department.objects.all()
    return render(request, 'departments/list.html', {'departments': departments})

