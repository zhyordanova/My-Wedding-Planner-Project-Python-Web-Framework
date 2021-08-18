from django.core.exceptions import ValidationError

from my_wedding_planner.tasklist.models import Like
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestLikeModel(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testLikeModel__whenFormIsValid__shouldSave(self):
        self.client.force_login(self.user)
        task_user = self.create_user(
            email='test@user.com',
            password='test_password',
        )

        tasks = self.create_task(
            name='Test Task',
            quest_capacity='100',
            budget='1000',
            note='Test note',
            image='path/to/image.png',
            url='Test Url',
            category='TaskList.CATEGORY_CHOICE_RECEPTION',
            user=task_user,
        )

        like_data = {
            'task': tasks,
            'user': self.user,
        }

        like_object = Like(**like_data)
        like_object.full_clean()
        like_object.save()

        self.assertEqual(tasks, like_object.task)
        self.assertEqual(self.user, like_object.user)
        self.assertTrue(Like.objects.filter(task_id=tasks.id).exists())

    def testLikeForm__whenFormIsInValid__shouldReturnError(self):

        tasks = self.create_task(
            name='Test Task',
            quest_capacity='100',
            budget='1000',
            note='Test note',
            image='path/to/image.png',
            url='Test Url',
            category='TaskList.CATEGORY_CHOICE_RECEPTION',
            user=self.user,
        )

        like_data = {
            'task': tasks,
        }

        with self.assertRaises(ValidationError) as error:
            like_object = Like(**like_data)
            like_object.full_clean()
            like_object.save()

        self.assertIsNotNone(error)
        self.assertNotEqual(tasks.like_set, 0)
        self.assertFalse(Like.objects.filter(pk=self.user.id).exists())
