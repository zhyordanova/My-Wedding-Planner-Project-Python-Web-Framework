from django import forms
from django.contrib.auth.forms import UserChangeForm

from my_wedding_planner.core.bootstrap_form_mixin import BootstrapFormMixin
from my_wedding_planner.profiles.models import MyWeddingPlannerProfile


class PlannerProfileForm(BootstrapFormMixin, forms.ModelForm):
    """
    A form for creating new users. Include all the required fields, plus a repeated password.
    """

    class Meta:
        model = MyWeddingPlannerProfile
        exclude = ('user', 'is_complete')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': "First name",
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': "Last name",
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': "Age",
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': "e.g. '+999999999'",
                }
            ),
        }


# class ChangeProfileInfo(UserChangeForm):
#     def __init__(self, *args, **kwargs):
#         self.request = kwargs.pop('request', None)
#         super().__init__(*args, **kwargs)
#         self.field['profile_image'].label = 'Change Profile Image'
#
#     password = None
#
#     class Meta:
#         model = MyWeddingPlannerProfile
#         fields = ('profile_image', 'first_name', 'last_name', 'age', 'phone_number')
#         widgets = {
#             'profile_image': forms.FileInput(),
#         }
