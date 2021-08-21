from django.urls import path

from my_wedding_planner.tasklist.views import ListTasksView, task_like, task_comment, TaskDetailsView, CreateTaskView, \
    EditTaskView, DeleteTaskView

urlpatterns = [
    path('', ListTasksView.as_view(), name='list tasks'),
    path('like/<int:pk>', task_like, name='task like'),
    path('comment/<int:pk>', task_comment, name='task comment'),
    path('details/<int:pk>', TaskDetailsView.as_view(), name='task details'),
    path('create/', CreateTaskView.as_view(), name='create task'),
    path('edit/<int:pk>', EditTaskView.as_view(), name='edit task'),
    path('delete/<int:pk>', DeleteTaskView.as_view(), name='delete task'),
]
