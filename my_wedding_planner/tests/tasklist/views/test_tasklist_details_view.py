from django.urls import reverse

from tests.base.mixins import TaskTestUtils, UserTestUtils, LikeTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TaskDetails(TaskTestUtils, UserTestUtils, LikeTestUtils, MyWeddingPlannerTestCase):

    def testTaskDetails__whenTaskExistsAndIsOwner__shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        task = self.create_task(
            name='Test Task',
            quest_capacity='100',
            budget='1000',
            note='Test note',
            image='path/to/image.png',
            url='http://127.0.0.1:8000/tasks/details/1',
            category='TaskList.CATEGORY_CHOICE_RECEPTION',
            user=self.user,
        )

        response = self.client.get(reverse('task details', kwargs={
            'pk': task.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked_by_user'])

    def testTaskDetails__whenTaskExistsAndIsNotOwnerAndNotLiked__shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        task_user = self.create_user(
            email='test@user.com',
            password='test_password',
        )

        task = self.create_task(
            name='Test Task',
            quest_capacity='100',
            budget='1000',
            note='Test note',
            image='path/to/image.png',
            url='http://127.0.0.1:8000/tasks/details/2',
            category='TaskList.CATEGORY_CHOICE_TRANSPORTATION',
            user=task_user
        )

        response = self.client.get(reverse('task details', kwargs={
            'pk': task.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked_by_user'])

    def testTaskDetails__whenTaskExistsAndIsNotOwnerAndLiked__shouldReturnDetailsForOwner(self):
        self.client.force_login(self.user)
        task_user = self.create_user(
            email='test@user.com',
            password='test_password',
        )

        task = self.create_task_with_like(
            like_user=self.user,
            name='Test Task',
            quest_capacity='100',
            budget='1000',
            note='Test note',
            image='path/to/image.png',
            url='http://127.0.0.1:8000/tasks/details/3',
            category='TaskList.CATEGORY_CHOICE_CEREMONY',
            user=task_user
        )

        response = self.client.get(reverse('task details', kwargs={
            'pk': task.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked_by_user'])
