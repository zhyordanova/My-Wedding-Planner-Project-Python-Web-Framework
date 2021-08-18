from django.urls import reverse

from tests.base.tests import MyWeddingPlannerTestCase


class TestCreateTaskView(MyWeddingPlannerTestCase):

    def testCreateTask__whenUserIsNotLoggedIn__shouldRedirectTheUser(self):
        response = self.client.get(reverse('create task'))
        self.assertEqual(response.status_code, 302)

    def testCreateTask__whenUserIsLoggedIn__shouldAddTheTaskToTheList(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasklist/task_create.html')

