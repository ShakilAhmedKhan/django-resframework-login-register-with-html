# task_manager/views.py
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from .models import Task, TaskImage
from .forms import TaskForm, TaskFilterForm, TaskImageForm
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

        # Sorting tasks by priority or due date
        sort_param = request.GET.get('sort', None)
        if sort_param == 'priority':
            tasks = tasks.order_by('priority')
        elif sort_param == 'due_date':
            tasks = tasks.order_by('due_date')

        # Searching tasks by name
        search_param = request.GET.get('search', None)
        if search_param:
            tasks = tasks.filter(Q(title__icontains=search_param))



        return render(request, 'task_list.html', {'tasks': tasks})

from django.views import View
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

class TaskCreateView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = TaskForm()
        image_form = TaskImageForm()
        return render(request, 'task_create.html', {'form': form, 'image_form': image_form})

    def post(self, request):
        form = TaskForm(request.POST)
        # form = TaskForm(request.POST, request.FILES)
        image_form = TaskImageForm(request.POST, request.FILES)
        if form.is_valid() and image_form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user  # Assign the currently logged-in user as the creator
            task.save()

            for img in request.FILES.getlist('image'):
                TaskImage.objects.create(task=task, image=img)

            return redirect('task_list')
        return render(request, 'task_create.html', {'form': form, 'image_form': image_form})


class TaskUpdateView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        image_form = TaskImageForm()  # Create an empty image form
        return render(request, 'task_update.html', {'form': form, 'task': task, 'image_form': image_form})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        image_form = TaskImageForm(request.POST, request.FILES)

        if form.is_valid() and image_form.is_valid():
            # task.taskimage_set.all().delete()
            old_images = TaskImage.objects.filter(task=task)
            old_images.delete()
            form.save()

            for img in request.FILES.getlist('image'):
                TaskImage.objects.create(task=task, image=img)

            return redirect('task_list')

        return render(request, 'task_update.html', {'form': form, 'task': task, 'image_form': image_form})


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