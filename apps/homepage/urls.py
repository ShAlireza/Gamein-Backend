from django.urls import path

from .views import *

urlpatterns = [
    path('', view=homepage, name='Homepage'),
    path('staffs/', view=staffs, name='Staffs')
]
