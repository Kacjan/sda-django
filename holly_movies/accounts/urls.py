from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginViewCustom, PasswordChangeViewCustom, SignUpView


urlpatterns = [
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeViewCustom.as_view(), name='password_change_view'),
    path('sign-up/', SignUpView.as_view(), name='sign_up')
]