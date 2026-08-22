from django.urls import path
from apps.accounts.views import (
    AccountUserRegistration,
    AccountUserLogin,
    AccountUserLogout,
)

urlpatterns = [
    path('register/', AccountUserRegistration.as_view(), name='register'),
    path('login/', AccountUserLogin.as_view(), name='login'),
    path('logout/', AccountUserLogout.as_view(), name='logout'),
    # path('info/', Info.as_view(), name='info'),
]