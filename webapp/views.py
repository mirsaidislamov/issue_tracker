from django.shortcuts import render
from django.views.generic import TemplateView

from webapp.models import Task


class TaskListView(TemplateView):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context

def task_list_view(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {
        'tasks': tasks
    })
