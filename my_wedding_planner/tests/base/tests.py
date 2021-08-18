from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from my_wedding_planner.tasklist.models import TaskList

UserModel = get_user_model()


class MyWeddingPlannerTestCase(TestCase):
    logged_in_user_email = 'wedding@planner.com'
    logged_in_user_password = 'wedding_planner'

    def assertListEmpty(self, wedding_list):
        return self.assertListEqual([], wedding_list, 'The Wedding TaskList not is empty')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password
        )
        self.user.is_active = True
        self.user.save()



