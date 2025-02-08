from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here
        return cleaned_data