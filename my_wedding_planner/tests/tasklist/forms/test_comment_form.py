from my_wedding_planner.tasklist.forms import CommentForm
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestCommentForm(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testCommentForm__whenFormIsValid__shouldSave(self):

        self.client.force_login(self.user)
        task_user = self.create_user(
            email='test@weddingplanner.com',
            password='passwordTest',
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

        form_comment_test = {
            'comment': 'testComment',
            'task_pk': task.id,
        }

        form = CommentForm(data=form_comment_test)
        self.assertTrue(form.is_valid())

    def testCommentForm__whenFormIsInValid__shouldReturnError(self):
        self.client.force_login(self.user)
        task_user = self.create_user(
            email='test@weddingplanner.com',
            password='passwordTest',
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

        form_comment_test = {
            'comment': '',
            'task_pk': task.id,
        }

        form = CommentForm(data=form_comment_test)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], ['This field is required.'])




