from my_wedding_planner.tasklist.forms import CreateTaskListForm
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestCreateTaskListForm(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testCreateTaskListForm__whenFormIsValid__shouldSave(self):

        self.client.force_login(self.user)
        task_user = self.create_user(
            email='test@weddingplanner.com',
            password='passwordTest',
        )

        form_task_test = {
            'name': 'Test Task',
            'quest_capacity': '100',
            'budget': '1000',
            'note': 'Test note',
            'image': 'path/to/image.png',
            'url': 'http://127.0.0.1:8000/tasks/create/',
            'category': 'Reception',
            'user': task_user,
        }

        form = CreateTaskListForm(data=form_task_test)
        self.assertTrue(form.is_valid())

    def testCreateTaskListForm__whenFormNotThereIsAnEmptyField__shouldRaiseError(self):

        self.client.force_login(self.user)
        task_user = self.create_user(
            email='test@weddingplanner.com',
            password='passwordTest',
        )

        form_task_test = {
            'name': '',
            'quest_capacity': '100',
            'budget': '1000',
            'note': 'Test note',
            'image': 'path/to/image.png',
            'url': 'http://127.0.0.1:8000/tasks/create/',
            'category': 'Reception',
            'user': task_user,
        }

        form = CreateTaskListForm(data=form_task_test)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])


