from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse

from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskListView(TemplateView):
    template_name = 'task/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskDetailView(DetailView):
    template_name = 'task/task_detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
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


class TaskDeleteView(DeleteView):
    template_name = 'task/task_delete.html'
    model = Task

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})
