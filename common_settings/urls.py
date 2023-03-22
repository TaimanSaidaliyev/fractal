from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('', UpdateInterface, name='update_interface'),
]