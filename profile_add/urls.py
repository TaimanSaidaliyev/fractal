from django.urls import path
from .views import *

urlpatterns = [
    #path('', index, name='home'),
    path('', ProfilePage, name='profile'),
    path('update_my_profile', update_profile, name='my_profile_edit'),
    path('update_profile/<int:pk>', update_profile, name='profile_edit'),
    path('<int:pk>', view_profile, name='profile_view'),
    path('user_all', view_all_users, name='profile_all_users'),
    path('start_time_tracking', time_tracking, name='start_time_tacking'),
    path('time_tracking_report', time_tracking_report, name='time_tacking_report'),
    path('time_tracking_report_js', time_tracking_js, name='time_tacking_report_js'),
    path('api', api, name='api')
]
