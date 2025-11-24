from django.db import models
from webapp.models import BaseModel


class Task(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.RESTRICT, verbose_name='Статус', related_name='tasks', blank=True, null=True)
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Типы', blank=True)
    project = models.ForeignKey('webapp.Project', on_delete=models.SET_NULL, related_name='tasks', verbose_name='Проект',blank=True, null=True)

    def __str__(self):
        return self.title