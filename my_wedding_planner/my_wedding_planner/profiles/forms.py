from django import forms

from my_wedding_planner.core.bootstrap_form_mixin import BootstrapFormMixin
from my_wedding_planner.profiles.models import MyWeddingPlannerProfile


class PlannerProfileForm(BootstrapFormMixin, forms.ModelForm):

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

