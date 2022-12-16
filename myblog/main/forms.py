from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class LoginPage_Form(forms.Form, LoginView):
    class Meta:
        models = User
        fields = ['username', 'email', 'password1', 'password2']