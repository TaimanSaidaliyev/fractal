from django.urls import path
from .views import *

urlpatterns = [
    path('', sing_in, name='signin'),
    path('logout', user_logout, name='exit'),
]