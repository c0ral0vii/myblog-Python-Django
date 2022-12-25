from django.contrib.auth import login, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
from django.shortcuts import redirect


from .forms import *
from .models import *


def home(request):
    if request.user.is_authenticated:
        context = {
            'title': 'home',
            'profile': Profile.objects.filter(username=request.user),
        }
    else:
        context = {
            'title': 'home',
        }

    return render(request, 'main/home.html', context=context)


def profile(request, user):
    context = {
        'title': 'profile',
        'profile': Profile.objects.filter(user=request.user),
    }
    return render(request, 'main/profile.html', context=context)


class RegisterPage(CreateView):
    form_class = RegisterUser_Form
    template_name = 'main/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register page'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginPage(LoginView):
    form_class = LoginUser_Form
    template_name = 'main/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login page'
        return context


def logout_(request):
    logout(request)
    return redirect('home')
