from my_wedding_planner.accounts.forms import RegisterForm
from tests.base.tests import MyWeddingPlannerTestCase


class TestRegisterForm(MyWeddingPlannerTestCase):

    def testRegisterForm__whenFormIsValid_ShouldSaveFormAndReturnTrue(self):
        form_register_test = {
            'email': 'test@weddingplaner.com',
            'password1': 'test_password',
            'password2': 'test_password',
        }

        form = RegisterForm(data=form_register_test)
        self.assertTrue(form.is_valid())

    def testRegisterForm__whenConfirmPasswordIsIncorrect__shouldReturnPasswordError(self):
        form_register_test = {
            'email': self.logged_in_user_email,
            'password1': self.logged_in_user_password,
            'password2': 'test_incorrect_password',
        }

        form = RegisterForm(data=form_register_test)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('password2'))
        self.assertEqual(form.errors['password2'], ['Passwords do not match, please try again.'])

    def testRegisterForm__whenIsEmpty__shouldReturnValidationError(self):
        form_register_test = {}
        form = RegisterForm(data=form_register_test)

        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['password1'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])
        self.assertFalse(form.is_valid())

    def testRegisterForm__whenEmailIsInvalid__shouldReturnValidationError(self):
        form_register_test = {
            'email': 'test_email.com',
            'password1': self.logged_in_user_password,
            'password2': self.logged_in_user_password,
        }

        form = RegisterForm(data=form_register_test)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertFalse(form.is_valid())
