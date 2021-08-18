from PIL import Image

from my_wedding_planner.tasklist.models import TaskList
from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestTaskList(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def setUp(self):
        task_user = self.create_user(
            email='test@user.com',
            password='test_password',
        )

        self.task = TaskList.objects.create(
            name='Test Task Edit',
            quest_capacity=300,
            budget=5000,
            note='Test Note Edit',
            image='path/to/image.png',
            url='http://127.0.0.1:8000/tasks/',
            category='Entertainment',
            user=task_user,
        )

    def testTaskList__whenModelFieldsTypeSetCorrect__shouldReturnValidModel(self):
        self.assertIsInstance(self.task.name, str)
        self.assertTrue(self.task.quest_capacity, int)
        self.assertTrue(self.task.budget, float)
        self.assertIsInstance(self.task.note, str)
        self.assertTrue(self.task.image, Image)
        self.assertTrue(self.task.url, str)
        self.assertIsInstance(self.task.category, str)

    def testTaskList__whenModelFieldsTypeSet__shouldReturnBuildInvalidations(self):
        self.assertEqual(self.task._meta.get_field('name').max_length, 100)
        self.assertEqual(self.task._meta.get_field('image').upload_to, 'tasklist')
        self.assertEqual(self.task._meta.get_field('url').max_length, 200)
        self.assertEqual(self.task._meta.get_field('category').max_length, 100)

    def testTaskList__whenUserSettingBudgetToNegativeValue__shouldRaiseValidatorError(self):
        profile = TaskList(
            budget=-3,
        )

        self.assertTrue('Ensure this value is greater than or equal to %(limit_value)s.')

    def testTaskList__whenUserSettingBudgetToPositiveValue__shouldSetTheBudget(self):
        profile = TaskList(
            budget=3000,
        )

        self.assertTrue(self.task.budget, 3000)

    def testTaskList__whenUserGivingNegativeValueGuestCapacity__shouldRaiseValidatorError(self):
        profile = TaskList(
            quest_capacity=-3,
        )

        self.assertTrue('Ensure this value is greater than or equal to %(limit_value)s.')

    def testTaskList__whenUserSettingPositiveValueGuestCapacity__shouldSetGuestCapacity(self):
        profile = TaskList(
            quest_capacity=3000,
        )

        self.assertTrue(3000, self.task.quest_capacity)
