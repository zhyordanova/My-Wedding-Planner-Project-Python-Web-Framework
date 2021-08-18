from django.urls import reverse

from my_wedding_planner.profiles.models import MyWeddingPlannerProfile
from tests.base.mixins import TaskTestUtils
from tests.base.tests import MyWeddingPlannerTestCase


class TestProfileDetails(TaskTestUtils, MyWeddingPlannerTestCase):

    def testProfileDetailsView_name_and_templateName(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('dashboard profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='profiles/dashboard_profiles.html')

    def testProfileDetailsView__whenLoggedInUserAndDidNotCreateTaskYet__shouldGetDashboardWithoutTasks(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('dashboard profile'))

        self.assertEqual(response.status_code, 200)
        self.assertListEmpty(list(response.context['tasks']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def testProfileDetails__whenLoggedInUserAndCreateTask__shouldGetDashboardWithTasks(self):
        task = self.create_task(
            name='Test Task',
            quest_capacity='100',
            budget='1000',
            note='Test note',
            image='path/to/image.png',
            url='Test Url',
            category='Task.CATEGORY_CHOICE_RECEPTION',
            user=self.user,
        )

        self.client.force_login(self.user)

        response = self.client.get(reverse('dashboard profile'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual([task], list(response.context['tasks']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

    def testProfileDetails__whenUserLoggedInWithImage__shouldChangeDefaultImage(self):
        path_to_image = 'path/to/image.png'
        profile = MyWeddingPlannerProfile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image + 'old'
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('dashboard profile'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(response.status_code, 302)
        profile = MyWeddingPlannerProfile.objects.get(pk=self.user.id)

    def test_postDashboard__whenUserLoggedInWithoutImage__shouldNotChangeDefaultImage(self):
        path_to_image = 'path/to/image.png'
        profile = MyWeddingPlannerProfile.objects.get(pk=self.user.id)
        profile.profile_image = path_to_image
        profile.save()

        self.client.force_login(self.user)

        response = self.client.post(reverse('dashboard profile'), data={
            'profile_image': path_to_image,
        })

        self.assertEqual(200, response.status_code)


class TestDeleteProfileView(MyWeddingPlannerTestCase):

    def test__whenDeleteProfile__shouldReturnQuestion(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete profile', args=(self.user.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Are you sure you want to delete your profile?")

    def test__whenSuccessfulDeleteProfile__shouldDeleteTheProfile(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete profile', args=(self.user.id,)))

        self.assertEqual(response.status_code, 200)
