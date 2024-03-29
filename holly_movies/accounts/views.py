from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserCreationFormCustom

class LoginViewCustom(LoginView):
    template_name = 'login.html'


class PasswordChangeViewCustom(PasswordChangeView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('login')


class SignUpView(CreateView):
    template_name = 'create_account.html'
    form_class = UserCreationFormCustom
    success_url = reverse_lazy('index')
