from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from my_wedding_planner.accounts.forms import LoginForm, RegisterForm
from my_wedding_planner.accounts.models import MyWeddingPlannerUser


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse('index')


class RegisterUserView(CreateView):
    model = MyWeddingPlannerUser
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard profile')
    context_object_name = 'form'

    def form_valid(self, form):
        result = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=email, password=password)

        login(self.request, new_user)

        return result


def logout_user(request):
    logout(request)
    return redirect('index')

