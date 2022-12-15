from django.shortcuts import render
from django.views.generic import CreateView

from .forms import *


def home(request):
    return render(request, 'home.html')


class LoginPage(CreateView, LoginView):
    form_class = LoginPage_Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login page'
        return context