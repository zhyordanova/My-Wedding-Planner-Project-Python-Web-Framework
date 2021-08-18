from django.urls import reverse

from tests.base.mixins import TaskTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestEditTaskView(TaskTestUtils, MyWeddingPlannerTestCase):

    def testEditTask__whenUserIsOwner__shouldEditSuccessfully(self):
        self.client.force_login(self.user)

        task = self.create_task(
            name='Test Task Edit',
            quest_capacity=300,
            budget=5000,
            note='Test Note Edit',
            image='path/to/image.png',
            url='http://127.0.0.1:8000/tasks/edit/',
            category='TaskList.CATEGORY_CHOICE_ATTIRE_AND_ACCESSORIES',
            user=self.user,
        )
        response = self.client.get(reverse('edit task', kwargs={
            'pk': task.id,
        }))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasklist/task_edit.html')