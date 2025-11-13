from django import forms

from webapp.models import Task, Status, Type


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', required=True)
        types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', required=True)
        fields = ['title', 'description', 'status', 'type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
