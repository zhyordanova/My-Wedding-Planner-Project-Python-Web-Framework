from my_wedding_planner.accounts.forms import LoginForm
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestLoginForm(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testLogInForm__whenIsValid__shouldReturnTrue(self):
        form_login_test = {
            'username': self.logged_in_user_email,
            'password': self.logged_in_user_password,
        }

        form = LoginForm(data=form_login_test)
        self.assertTrue(form.is_valid())

    def testLogInForm__whenEmailIsEmpty__shouldReturnValidationError(self):
        form_login_test = {
            'email': '',
            'password': self.logged_in_user_password,
        }

        form = LoginForm(data=form_login_test)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def testLogInForm__whenPasswordIsEmpty__shouldReturnValidationError(self):
        form_login_test = {
            'email': self.logged_in_user_email,
            'password': '',
        }

        form = LoginForm(data=form_login_test)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])





