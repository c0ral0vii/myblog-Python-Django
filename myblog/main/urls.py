from django.urls import path

from .views import *


urlpatterns = [
    path('home/', home, name='home'),
    path('login/', LoginView.as_view(), name='login'),
]