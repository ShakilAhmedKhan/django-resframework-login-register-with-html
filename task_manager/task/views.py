# task_manager/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm, TaskFilterForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskListView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        user = request.user  # Get the currently logged-in user

        user = user.id
        # print(user.id)
        # tasks = Task.objects.filter(created_by=user.id)
        tasks = Task.objects.filter(created_by=user)


        return render(request, 'task_list.html', {'tasks': tasks})
        # tasks = Task.objects.all()
        # print(user.id)
        # return render(request, 'task_list.html', {'tasks': tasks})

class TaskCreateView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'task_create.html', {'form': form})

# Create views for task details, update, and delete similarly
# class TaskCreateView(View):
#     def get(self, request):
#         form = TaskForm()
#         return render(request, 'task_create.html', {'form': form})
#
#     def post(self, request):
#         form = TaskForm(request.POST, request.FILES)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.created_by = request.user  # Assign the currently logged-in user as the creator
#             task.save()
#             return redirect('task_list')
#         return render(request, 'task_create.html', {'form': form})

# task_manager/views.py

from django.views import View
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

class TaskCreateView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user  # Assign the currently logged-in user as the creator
            task.save()
            return redirect('task_list')
        return render(request, 'task_create.html', {'form': form})


class TaskUpdateView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, 'task_update.html', {'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'task_update.html', {'form': form, 'task': task})


class TaskDeleteView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')


class TaskDetailsView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_details.html', {'task': task})
