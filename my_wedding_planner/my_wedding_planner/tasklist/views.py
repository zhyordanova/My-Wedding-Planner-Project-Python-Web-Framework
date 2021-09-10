from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from my_wedding_planner.tasklist.forms import CommentForm, CreateTaskListForm, EditTaskListForm
from my_wedding_planner.tasklist.models import TaskList, Like, Comment


class ListTasksView(ListView):
    template_name = 'tasklist/tasks_list.html'
    context_object_name = 'tasks'
    model = TaskList
    paginate_by = 3


class TaskDetailsView(DetailView):
    template_name = 'tasklist/task_details.html'
    context_object_name = 'tasks'
    model = TaskList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = context[self.context_object_name]

        task.likes_count = task.like_set.count()

        context['comment_form'] = CommentForm(
            initial={
                'task_pk': self.object.id,
            }
        )
        context['comments'] = task.comment_set.all()
        context['is_owner'] = task.user == self.request.user
        context['is_liked_by_user'] = task.like_set.filter(user_id=self.request.user.id)\
            .exists()

        return context


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'tasklist/task_create.html'
    model = TaskList
    form_class = CreateTaskListForm
    success_url = reverse_lazy('list tasks')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super().form_valid(form)


class EditTaskView(LoginRequiredMixin, UpdateView):
    template_name = 'tasklist/task_edit.html'
    model = TaskList
    form_class = EditTaskListForm
    success_url = reverse_lazy('list tasks')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    template_name = 'tasklist/task_delete.html'
    model = TaskList
    success_url = reverse_lazy('list tasks')


@login_required(login_url=reverse_lazy('login'))
def task_like(request, pk):
    task = TaskList.objects.get(pk=pk)
    like_object_by_user = task.like_set.filter(user_id=request.user.id) \
        .first()

    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            task=task,
            user=request.user,
        )

        like.save()

    return redirect('task details', task.pk)


@login_required(login_url=reverse_lazy('login'))
def task_comment(request, pk):
    task = TaskList.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            comment=form.cleaned_data['comment'],
            task=task,
            user=request.user,
        )

        comment.save()

    return redirect('task details', task.pk)
