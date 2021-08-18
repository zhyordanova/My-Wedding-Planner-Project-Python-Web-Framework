from django.urls import reverse

from my_wedding_planner.tasklist.models import Like
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestLikeTaskVIew(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testLikeTask__whenTaskNotLiked_shouldCreateLike(self):
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
            url='Test Url',
            category='TaskList.CATEGORY_CHOICE_RECEPTION',
            user=task_user,
        )

        response = self.client.post(reverse('task like', kwargs={
            'pk': task.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            task_id=task.id,
        )\
            .exists()

        self.assertTrue(like_exists)

    def testLikeTask__whenTaskAlreadyLiked_shouldDeleteTheLike(self):
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
            url='http://127.0.0.1:8000/tasks/like/',
            category='TaskList.CATEGORY_CHOICE_DECORATION',
            user=task_user,
        )

        response = self.client.post(reverse('task like', kwargs={
            'pk': task.id,
        }))

        self.assertEqual(302, response.status_code)

        like_exists = Like.objects.filter(
            user_id=self.user.id,
            task_id=task.id,
        ) \
            .exists()

        self.assertFalse(like_exists)
