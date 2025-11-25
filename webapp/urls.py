from django.urls import path

from webapp.views import TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, ProjectListView, ProjectDetailView, ProjectCreateView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create', ProjectCreateView.as_view(), name='project_create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]