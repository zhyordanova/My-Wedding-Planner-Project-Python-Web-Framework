from datetime import datetime

from tests.base.tests import MyWeddingPlannerTestCase


class TestMyWeddingPlannerUser(MyWeddingPlannerTestCase):

    def testAccountModel__whenUserFieldsAreSet__shouldGetFieldsType(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.date_joined, datetime)
        self.assertIsInstance(self.user.last_login, datetime)
        self.assertIsInstance(self.user.is_active, bool)
        self.assertIsInstance(self.user.is_staff, bool)
        self.assertIsInstance(self.user.is_superuser, bool)

    def testAccountModel__whenUserFieldsAreSet__shouldGetBuildInValidations(self):
        self.assertTrue(self.user._meta.get_field('email').unique)
        self.assertTrue(self.user._meta.get_field('date_joined').auto_now_add)
        self.assertTrue(self.user._meta.get_field('last_login').auto_now)
        self.assertTrue(self.user._meta.get_field('is_active').default)
        self.assertFalse(self.user._meta.get_field('is_staff').default)
        self.assertFalse(self.user._meta.get_field('is_superuser').default)