from django import forms
from django.contrib.auth.views import LoginView


class LoginPage_Form(forms.Form, LoginView):
    class Meta:
        models = User
        fields = ['username', 'email', 'password1', 'password2']