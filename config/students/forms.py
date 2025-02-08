from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here
        return cleaned_data