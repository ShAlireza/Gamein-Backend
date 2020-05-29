from django.urls import path

from .views import *

urlpatterns = [
    path('', view=HomepageView.as_view(), name='Homepage'),
    path('staffs/', view=StaffsView.as_view(), name='Staffs')
]
