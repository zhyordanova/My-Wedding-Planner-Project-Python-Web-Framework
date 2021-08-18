from django.urls import reverse

from tests.base.mixins import TaskTestUtils, UserTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestLogOutView(TaskTestUtils, UserTestUtils, MyWeddingPlannerTestCase):

    def testLogOut_shouldReturnToIndexPage(self):
        self.client.force_login(self.user)
        log_out = self.client.get(reverse('logout'))

        self.assertEqual(log_out.status_code, 302)
