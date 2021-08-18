import os
from os.path import join

from django import forms
from django.conf import settings

from my_wedding_planner.core.bootstrap_form_mixin import BootstrapFormMixin
from my_wedding_planner.tasklist.models import TaskList, Comment


class TaskListForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = TaskList
        exclude = ('user',)


class CreateTaskListForm(TaskListForm):
    class Meta:
        model = TaskList
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Enter the name of specific place you want to check later...",
                }
            ),
            'quest_capacity': forms.NumberInput(
                attrs={
                    'placeholder': "Enter approximate quests count you would like to invite...",
                }
            ),
            'budget': forms.NumberInput(
                attrs={
                    'placeholder': "Enter approximate budget you are planning to spend...",
                }
            ),
            'note': forms.TextInput(
                attrs={
                    'placeholder': "Enter a short explanation what impressed you in this place...",
                }
            ),
            'url': forms.URLInput(
                attrs={
                    'placeholder': "Enter a web page or social media...",
                }
            ),
        }


class EditTaskListForm(TaskListForm):
    def save(self, commit=True):
        db_tasklist = TaskList.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_tasklist.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = TaskList
        exclude = ('user',)
        widgets = {
            'category': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }


class CommentForm(BootstrapFormMixin, forms.ModelForm):
    task_pk = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = Comment
        fields = ('comment', 'task_pk')
        widgets = {
            'comment': forms.TextInput(
                attrs={
                    'placeholder': 'Let me know what do you think about ...'
                }
            ),
        }
