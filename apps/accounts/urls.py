from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [

    path('login', view=obtain_auth_token, name='login'),
    path('signup', view=views.SignUpAPIView.as_view(), name='signup'),
    path('logout', view=views.LogoutAPIView.as_view(), name='logout'),
    path('activation-email', view=views.ResendActivationEmailAPIView.as_view(),
         name='resend_activation_email'),
    path('signup/activate', view=views.ActivateAccountAPIView.as_view(),
         name='activate_account'),
    path('reset-password', view=views.ResetPasswordAPIView.as_view(),
         name='reset_password'),
    path('reset-password/confirm',
         view=views.ResetPasswordConfirmAPIView.as_view(),
         name='reset_password_confirm'),
    path('profile/hide-info',
         view=views.ToggleProfileInfoVisibilityAPIView.as_view(),
         name='hide_profile_info'),

]
