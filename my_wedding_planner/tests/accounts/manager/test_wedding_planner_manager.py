from django.contrib.auth import get_user_model

from tests.base.tests import MyWeddingPlannerTestCase

UserModel = get_user_model()


class TestMyWeddingPlannerManager(MyWeddingPlannerTestCase):

    def testManager__whenCreatingUser__shouldReturnUser(self):
        tasks_user = UserModel.objects.create_user(
            email='test_wedding@planner.com',
            password='test_wedding_planner_2',
        )

        self.assertEqual(True, tasks_user.is_active)
        self.assertEqual(False, tasks_user.is_staff)
        self.assertEqual('test_wedding@planner.com', tasks_user.email)

    def testManager__whenCreateSuperuser__shouldReturnSuperuser(self):
        tasks_user = UserModel.objects.create_superuser(
            email='test_wedding@planner.com',
            password='test_wedding_planner_2',
        )

        self.assertEqual(True, tasks_user.is_superuser)
        self.assertEqual(True, tasks_user.is_staff)
        self.assertEqual('test_wedding@planner.com', tasks_user.email)

    def testManager__whenCreateUserAsUser__shouldNotReturnSuperuser(self):
        tasks_user = UserModel.objects.create_user(
            email='test_wedding@planner.com',
            password='test_wedding_planner_2',
        )

        self.assertEqual(True, tasks_user.is_active)
        self.assertEqual(False, tasks_user.is_superuser)
        self.assertEqual(False, tasks_user.is_staff)
        self.assertEqual('test_wedding@planner.com', tasks_user.email)
