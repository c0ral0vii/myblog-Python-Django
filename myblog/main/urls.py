from django.urls import path

from .views import *


urlpatterns = [
    path('home/', home, name='home'),
    path('register/', RegisterPage.as_view(), name='register'),
]