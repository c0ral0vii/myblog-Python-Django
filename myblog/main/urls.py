from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_, name='logout'),

    path('profile/<str:user>', profile, name='profile'),
]

if settings.DEBUG:
     urlpatterns += static(
         settings.STATIC_URL,
         document_root=settings.STATIC_ROOT
     )
     urlpatterns += static(
         settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT
     )