from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here
        return cleaned_data