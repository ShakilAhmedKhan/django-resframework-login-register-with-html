# task_manager/urls.py

from django.urls import path
from .views import TaskListView, TaskCreateView , TaskListView, TaskCreateView, TaskDetailsView, TaskUpdateView, TaskDeleteView
from .api import TaskListCreateAPI, TaskRetrieveUpdateDeleteAPI

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('api/tasks/', TaskListCreateAPI.as_view(), name='api_task_list_create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDeleteAPI.as_view(), name='api_task_retrieve_update_delete'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', TaskDetailsView.as_view(), name='task_details'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),

]
