from django.contrib.auth import get_user_model

from my_wedding_planner.accounts.models import MyWeddingPlannerUser
from my_wedding_planner.tasklist.models import TaskList, Like

UserModel = get_user_model()


class TaskTestUtils:
    def create_task(self, **kwargs):
        return TaskList.objects.create(**kwargs)

    def create_task_with_like(self, like_user, **kwargs):
        task = self.create_task(**kwargs)
        Like.objects.create(
            task=task,
            user=like_user,
        )
        return task


class UserTestUtils:
    def create_user(self, **kwargs):
        return MyWeddingPlannerUser.objects.create_user(**kwargs)

    def create_superuser(self, **kwargs):
        return UserModel.objects.create_superuser


class LikeTestUtils:
    def create_like(self, **kwargs):
        return Like.objects.create_like(**kwargs)
