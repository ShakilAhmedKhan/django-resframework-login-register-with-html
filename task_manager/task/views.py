# task_manager/views.py

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

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})

class TaskCreateView(View):
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

class TaskCreateView(View):
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


# class TaskUpdateView(View):
#     def get(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         form = TaskForm(instance=task)
#         return render(request, 'task_update.html', {'form': form, 'task': task})
#
#     def post(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         form = TaskForm(request.POST, request.FILES, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect('task_details', pk=task.pk)
#         return render(request, 'task_update.html', {'form': form, 'task': task})

class TaskUpdateView(View):
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
# class TaskDeleteView(View):
#     def get(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         return render(request, 'task_delete.html', {'task': task})
#
#     def post(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         task.delete()
#         return redirect('task_list')


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')
# task_manager/views.py

class TaskDetailsView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_details.html', {'task': task})

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        filter_form = TaskFilterForm(request.GET)

        if filter_form.is_valid():
            title = filter_form.cleaned_data.get('title')
            created_at = filter_form.cleaned_data.get('created_at')
            due_date = filter_form.cleaned_data.get('due_date')
            priority = filter_form.cleaned_data.get('priority')
            completed = filter_form.cleaned_data.get('completed')

            if title:
                tasks = tasks.filter(title__icontains=title)

            if created_at:
                tasks = tasks.filter(created_at__date=created_at)

            if due_date:
                tasks = tasks.filter(due_date=due_date)

            if priority:
                tasks = tasks.filter(priority=priority)

            if completed is not None:
                tasks = tasks.filter(completed=completed)

        return render(request, 'task_list.html', {'tasks': tasks, 'filter_form': filter_form})
