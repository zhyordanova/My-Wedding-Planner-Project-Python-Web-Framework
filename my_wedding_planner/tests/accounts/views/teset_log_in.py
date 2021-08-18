from django.urls import reverse

from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestLogInView(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testLogInView_name_and_templateName(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/login.html')

    def testLogIn__whenUserIsActive__shouldSuccessfulLoggedInUser(self):
        task_user = self.create_user(
            email='test@user.com',
            password='test_password',
        )

        response = self.client.post(reverse('login'), data={
            'username': 'test@user.com',
            'password': 'test_password',
        }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context['user'].is_authenticated)

    def testLogIn__whenUserIsNotActive__shouldNotLoggedInUser(self):
        task_user = self.create_user(
            email='test@user.com',
            password='test_password',
        )

        response = self.client.post(reverse('login'), data={
            'username': 'test1@user.com',
            'password': 'test_password',
        }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertFalse(response.context['user'].is_authenticated)


