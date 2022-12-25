from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_, name='logout'),

    path('profile/<str:user>', profile, name='profile'),
]