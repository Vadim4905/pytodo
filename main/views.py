from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DetailView
from .models import Task,Subtask
from django.shortcuts import render, redirect

from .forms import TaskForm

# crispy form


class IndexView(ListView):
    template_name = "main/index.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related('subtask_set').all()

    def get_context_data(self,*args,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Index'
        return context

class TaskVeiw(DetailView):
    template_name = "main/task_view.html"
    model = Task
    context_object_name = "task"

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        context['subtasks'] = Subtask.objects.filter(task=kwargs['object'])
        title = kwargs['object'].name
        context['title'] = f'Task {title}'
        return context

class TaskCreateView(CreateView):
    template_name = "main/task_create.html"
    form_class = TaskForm

    def form_valid(self, form: TaskForm) -> None:
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return redirect(to="/")
