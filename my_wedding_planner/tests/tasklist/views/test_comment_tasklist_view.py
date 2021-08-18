from django.urls import reverse

from my_wedding_planner.tasklist.models import TaskList
from tests.base.mixins import UserTestUtils, TaskTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestTaskCommentView(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def setUp(self):
        task_user = self.create_user(
            email='wedding@uplannerser.com',
            password='test_password',
        )

        self.task = TaskList.objects.create(
            name='Test Task Edit',
            quest_capacity=300,
            budget=5000,
            note='Test Note Edit',
            image='path/to/image.png',
            url='http://127.0.0.1:8000/tasks/comment/',
            category='TaskList.CATEGORY_CHOICE_ENTERTAINMENT',
            user=task_user,
        )

    def testCommentTask__whenUserIsPostingCommentAndIsNotOwner__shouldSaveAndRedirectToTaskDetails(self):
        user_not_owner = self.create_user(
            email='test@user.com',
            password='test_password',
        )

        task_comment = 'Test Comment'

        response = self.client.post(reverse('task comment', kwargs={
            'pk': self.task.id,
        }))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(task_comment, 'Test Comment')





