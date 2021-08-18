from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestRegisterView(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testRegisterView_name_and_templateName(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/register.html')

    def testRegisterUser__whenUserDoesNotExist__shouldRegisterTheUser(self):
        response = self.client.post(reverse('register'), data={
            'email': self.logged_in_user_email,
            'password1': self.logged_in_user_password,
            'password2': self.logged_in_user_password,
        })

        self.assertEqual(response.status_code, 200)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    def testRegisterUser__whenAlreadyExist__shouldNotCreateTheUser(self):

        response = self.client.post(reverse('register'), data={
            'email': self.logged_in_user_email,
            'password1': 'test_wedding_planner_password',
            'password2': 'test_wedding_planner_password',
        })

        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()

        self.assertEqual(users.count(), 1)

    # def testRegisterUser__whenPasswordsDoNotMatch__shouldRaiseValidationError(self):
    #     user = MyWeddingPlannerUser(
    #         email='test@user.com',
    #         password1='test_password',
    #         password2='Invalid Password',
    #     )
    #
    #     self.assertEqual(user, 'Passwords do not match, please try again.')

