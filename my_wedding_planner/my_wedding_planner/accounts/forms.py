from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UsernameField
from django.contrib.auth.hashers import check_password

from my_wedding_planner.core.bootstrap_form_mixin import BootstrapFormMixin

UserModel = get_user_model()


class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Include all the required fields, plus a repeated password.
    """

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match, please try again.')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    # def __init__(self, request, *args, **kwargs):
    #     # simply do not pass 'request' to the parent
    #     super().__init__(*args, **kwargs)

    def _init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                try:
                    user = UserModel.objects.get(email=username)
                    if not check_password(password, user.password):
                        raise forms.ValidationError(
                            {'password': 'Your Wedding Planner Password is incorrect.'}
                        )
                    elif not user.is_active:
                        raise forms.ValidationError(
                            {'username': 'Your Wedding Planner Account is inactive.'}
                        )
                except UserModel.DoesNotExist:
                    raise forms.ValidationError(
                        {'username': 'Your Wedding Planner Email is incorrect'}
                    )

        return super(LoginForm, self).clean()

    def save(self):
        return self.user

    username = UsernameField(
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'placeholder': 'wedding_planner@email.com',
            }))

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'e.g. ********',
            }))

    # error_messages = {
    #     'invalid_login': (
    #         "Please enter a correct %(username)s and password. Note that both "
    #         "fields may be case-sensitive."
    #     ),
    #     'inactive': ("This account is inactive."),
    # }

    # def __init__(self, *args, **kwargs):
    #     self.error_messages['invalid_login'] = f"Please enter a correct %(username)s and password. Note that both " \
    #                                            f"fields may be case-sensitive. "
    #     self.user = None
    #     super().__init__(*args, **kwargs)
    #
    # def clean(self):
    #     email = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #
    #     if email is not None and password:
    #         self.user_cache = authenticate(self.request, email=email, password=password)
    #         if self.user_cache is None:
    #             raise self.get_invalid_login_error()
    #         else:
    #             self.confirm_login_allowed(self.user_cache)
    #
    #     return self.cleaned_data


class RegisterForm(BootstrapFormMixin, UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'wedding_planner@email.com',
            }
        ),
        label='Enter your email',
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'e.g. ********',
            }
        ),
        label='Enter your password',
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter the same password, for verification',
            }
        ),
        label='Confirm your password',
    )


class ChangeUserInfo(UserChangeForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.field['profile_image'].label = 'Change Profile Image'

    password = None

    class Meta:
        model = UserModel
        fields = '__all__'
        widgets = {
            'profile_image': forms.FileInput(),
        }
