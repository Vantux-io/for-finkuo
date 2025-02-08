from django import forms
from .models import Subject

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here
        return cleaned_data