from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View

from webapp.forms import TaskForm
from webapp.models import Task


class TaskListView(TemplateView):
    template_name = 'task/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskDetailView(TemplateView):
    template_name = 'task/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        return context


class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task/task_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.id)
        else:
            return render(request, 'task/task_add.html', {'form': form})


class TaskUpdateView(View):

    def get(self, request, *args, pk,**kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'task/task_update.html', {'form': form})

    def post(self, request, *args, pk, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.id)
        return render(request, 'task/task_update.html', {'form': form, 'task': task})


class TaskDeleteView(View):

    def get(self, request, *args, pk,**kwargs):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task/task_delete.html', {'task': task})

    def post(self, request, *args, pk,**kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')
