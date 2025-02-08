from django.shortcuts import render, redirect
from .forms import GroupForm
from .models import Group


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_groups')  # Redirect to dashboard after saving
    else:
        form = GroupForm()
    return render(request, 'groups/form.html', {'form': form})


def list_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})

