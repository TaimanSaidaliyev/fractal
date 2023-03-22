from django.urls import path
from .views import *

urlpatterns = [
    path('', menu, name='Menu')
]
