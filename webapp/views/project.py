from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from django.shortcuts import reverse

from webapp.forms import SearchForm
from webapp.forms.project import ProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, object_list = None,**kwargs):
        context = super().get_context_data(object_list=object_list,**kwargs)
        context['search_form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        search_value = ''
        if self.search_form.is_valid():
            search_value = self.search_form.cleaned_data.get('search', '')
        return search_value


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        project = self.object
        context['tasks'] = project.tasks.all()
        return context


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    form_class = ProjectForm
