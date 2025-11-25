from django.db import models
from django.urls import reverse


class Project(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})