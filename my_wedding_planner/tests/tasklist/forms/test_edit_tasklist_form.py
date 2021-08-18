from my_wedding_planner.tasklist.forms import CreateTaskListForm, EditTaskListForm
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestEditTaskListForm(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testEditForm__whenEditTheData__shouldChangeTheData(self):
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

        create_form = CreateTaskListForm(data=form_task_test)
        self.assertTrue(create_form.is_valid())

        form_edit_test = {
            'name': 'Test Task Edit',
            'quest_capacity': '300',
            'budget': '5000',
            'note': 'Test Note Edit',
            'image': 'path/to/image2.png',
            'url': 'http://127.0.0.1:8000/tasks/edit/1',
            'category': 'Entertainment',
            'user': task_user,
        }

        edit_form = EditTaskListForm(data=form_edit_test)
        self.assertNotEqual(create_form.data['name'], edit_form.data['name'])
        self.assertEqual('Test Task Edit', edit_form.data['name'])
        self.assertNotEqual(create_form.data['quest_capacity'], edit_form.data['quest_capacity'])
        self.assertEqual('300', edit_form.data['quest_capacity'])
        self.assertNotEqual(create_form.data['budget'], edit_form.data['budget'])
        self.assertEqual('5000', edit_form.data['budget'])
        self.assertNotEqual(create_form.data['note'], edit_form.data['note'])
        self.assertEqual('Test Note Edit', edit_form.data['note'])
        self.assertNotEqual(create_form.data['image'], edit_form.data['image'])
        self.assertEqual('path/to/image2.png', edit_form.data['image'])
        self.assertNotEqual(create_form.data['url'], edit_form.data['url'])
        self.assertEqual('http://127.0.0.1:8000/tasks/edit/1', edit_form.data['url'])
        self.assertNotEqual(create_form.data['category'], edit_form.data['category'])
        self.assertEqual('Entertainment', edit_form.data['category'])
        self.assertEqual(create_form.data['user'], edit_form.data['user'])
