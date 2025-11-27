from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.forms import TaskForm
from webapp.models import Task, Project


class TaskDetailView(DetailView):
    template_name = 'task/task_detail.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/task_add.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'task/task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'task/task_delete.html'
    model = Task

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.project.pk})
