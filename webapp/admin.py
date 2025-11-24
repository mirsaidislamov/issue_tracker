from django.contrib import admin

from webapp.models import Task, Status, Type, Project


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status','created_at')
    list_filter = ('status', 'types','created_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['name', 'description']