from django.urls import path
from apps.accounts.views import (
    AccountUserRegistration,
    AccountUserLogin
)

urlpatterns = [
    path('register/', AccountUserRegistration.as_view(), name='register'),
    path('login/', AccountUserLogin.as_view(), name='login'),
    # path('logout/', Log_out.as_view(), name='logout'),
    # path('info/', Info.as_view(), name='info'),
]