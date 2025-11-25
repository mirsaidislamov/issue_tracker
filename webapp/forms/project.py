from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['start_date', 'end_date','name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','rows':'4'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError(
                    "Дата окончания не может быть раньше даты начала проекта."
                )