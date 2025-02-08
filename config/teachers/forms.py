from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here
        return cleaned_data