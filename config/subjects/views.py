from django.shortcuts import render, redirect
from .forms import SubjectForm
from .models import Subject


def add_subject(request):       
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_subjects')  # Redirect to dashboard after saving
    else:
        form = SubjectForm()
    return render(request, 'subjects/form.html', {'form': form})



def list_subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects': subjects})

