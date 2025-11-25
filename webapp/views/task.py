from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView
from django.urls import reverse

from webapp.forms import TaskForm
from webapp.models import Task, Project


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


class TaskCreateView(CreateView):
    template_name = 'task/task_add.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    template_name = 'task/task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(View):

    def get(self, request, *args, pk,**kwargs):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task/task_delete.html', {'task': task})

    def post(self, request, *args, pk,**kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('project_list')
