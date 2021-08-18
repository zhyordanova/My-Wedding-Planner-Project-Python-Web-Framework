from my_wedding_planner.profiles.forms import PlannerProfileForm
from tests.base.tests import MyWeddingPlannerTestCase


class TestPlannerProfileForm(MyWeddingPlannerTestCase):

    def testPlannerProfileForm_whenValid_shouldSave(self):
        form_profile_test = {
            'first_name': "Zhivka",
            'last_name': 'Yordnova',
            'phone_number': '+0878796789',
            'age': '33',
        }

        form = PlannerProfileForm(data=form_profile_test)
        self.assertTrue(form.is_valid())

    def testPlannerProfileForm__whenGivenWrongData__shouldReturnError(self):
        form_profile_test = {
            'first_name': "ZhivkaZhivkaZhivkaZhivkaZhivkaZhivka",
            'last_name': 'Yordnova',
            'phone_number': '+0878796789',
            'age': '33',
        }

        form = PlannerProfileForm(data=form_profile_test)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('first_name'))
        print(form.errors)

    def testPlannerProfileForm__whenGivenWrongPhoneNumber__shouldReturnError(self):
        form_profile_test = {
            'first_name': "Zhivka",
            'last_name': 'Yordnova',
            'phone_number': '00878796789vsdvdz99959456dgdgf21651',
            'age': '33',
        }

        form = PlannerProfileForm(data=form_profile_test)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('phone_number'))
        print(form.errors)
