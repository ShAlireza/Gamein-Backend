from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [

    path('login', view=obtain_auth_token, name='login'),
    path('signup', view=views.SignUpAPIView.as_view(), name='signup'),

]
