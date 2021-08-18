from django.contrib.auth import get_user_model

from my_wedding_planner.profiles.models import MyWeddingPlannerProfile
from tests.base.tests import MyWeddingPlannerTestCase

UserModel = get_user_model()


class TestMyWeddingPlannerProfileModel(MyWeddingPlannerTestCase):

    def testProfileModel__whenUserIsLoggingWithoutProfileData__shouldNoSetAnything(self):
        profile = MyWeddingPlannerProfile.objects.get(pk=self.user.id)

        self.assertEqual('', profile.first_name)
        self.assertEqual('', profile.last_name)
        self.assertEqual(None, profile.phone_number)
        self.assertEqual(None, profile.age)
        self.assertEqual('', profile.profile_image)
        self.assertEqual(self.user, profile.user)
        self.assertFalse(profile.is_complete)
        self.assertTrue(MyWeddingPlannerProfile.objects.filter(pk=self.user.id).exists())

    def testProfileModel__whenUserUpdatingProfileData__shouldSetData(self):
        profile = MyWeddingPlannerProfile(
            first_name='TestFirstName',
            last_name='TestLastName',
            age=33,
            phone_number='+99999999999',
            profile_image='path/to/image',
            user=self.user,
            is_complete=True,
        )

        self.assertEqual('TestFirstName', profile.first_name)
        self.assertEqual('TestLastName', profile.last_name)
        self.assertEqual(33, profile.age)
        self.assertEqual('+99999999999', profile.phone_number)
        self.assertEqual('path/to/image', profile.profile_image)
        self.assertEqual(self.user, profile.user)
        self.assertTrue(profile.is_complete)
        self.assertTrue(MyWeddingPlannerProfile.objects.filter(pk=self.user.id).exists())

    def testProfileModel__whenReturnStrRepresentation__shouldReturnFistNameAndLastName(self):
        profile = MyWeddingPlannerProfile(
            first_name='TestFirstName',
            last_name='TestLastName',
        )

        self.assertEqual(str(profile), 'TestFirstName TestLastName')

    def test__whenUserSettingAgeToNegativeValue__shouldRaiseBuildInErrorFromValidator(self):
        profile = MyWeddingPlannerProfile(
            age=-3,
        )

        self.assertTrue('Ensure this value is greater than or equal to %(limit_value)s.')





