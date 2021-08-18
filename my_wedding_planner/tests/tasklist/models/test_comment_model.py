from django.core.exceptions import ValidationError

from my_wedding_planner.tasklist.models import Comment
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestCommentTaskList(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testCommentModel__whenFormIsValid__shouldSave(self):
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

        comment_data = {
            'comment': 'testComment',
            'task': tasks,
            'user': self.user,
        }

        comment_object = Comment(**comment_data)
        comment_object.full_clean()
        comment_object.save()

        self.assertEqual(tasks, comment_object.task)
        self.assertEqual(self.user, comment_object.user)
        self.assertTrue(Comment.objects.filter(task_id=tasks.id).exists())

    def testCommentForm__whenFormIsInValid__shouldReturnError(self):

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

        comment_data = {
            'comment': '',
            'task': tasks,
            'user': self.user,
        }

        with self.assertRaises(ValidationError) as error:
            comment_object = Comment(**comment_data)
            comment_object.full_clean()
            comment_object.save()

        self.assertIsNotNone(error)
        self.assertFalse(Comment.objects.filter(pk=self.user.id).exists())


