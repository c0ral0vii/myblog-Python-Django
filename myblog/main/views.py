from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


def home(request):
    return render(request, 'main/home.html')


class RegisterPage(CreateView):
    form_class = RegisterUser_Form
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register page'
        return context