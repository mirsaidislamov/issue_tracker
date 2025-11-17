from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.RESTRICT, verbose_name='Статус', related_name='tasks', blank=True, null=True)
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Типы', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title



class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

