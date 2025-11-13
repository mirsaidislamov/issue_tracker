from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View

from webapp.forms import TaskForm
from webapp.models import Task


class TaskListView(TemplateView):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskDetailView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return context


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.id)
        else:
            return render(request, 'task_add.html', context={'form': form})
