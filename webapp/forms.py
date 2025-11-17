from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Task, Status, Type


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Статус', required=True)
        types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='Тип', required=True)
        fields = ['title', 'description', 'status', 'types']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'types': forms.CheckboxSelectMultiple(),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        forbidden_words = ['какие-то','запрещенные', 'запрещённые', 'слова']

        if title:
            title_lower = title.lower()
            for word in forbidden_words:
                if word in title_lower:
                    raise ValidationError(
                        f'Заголовок содержит запрещённое слово: "{word}". '
                    )
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()

        if description and len(description) < 10:
            raise ValidationError('Описание слишком короткое — минимум 10 символов.')