from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class Project(models.Model):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=100, verbose_name='Название проекта')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name



class Task(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.RESTRICT, verbose_name='Статус', related_name='tasks', blank=True, null=True)
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Типы', blank=True)
    project = models.ForeignKey('webapp.Project', on_delete=models.SET_NULL, related_name='tasks', verbose_name='Проект',blank=True, null=True)

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

