from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.hashers import check_password

from my_wedding_planner.core.bootstrap_form_mixin import BootstrapFormMixin

UserModel = get_user_model()


class LoginForm(BootstrapFormMixin, AuthenticationForm):

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

