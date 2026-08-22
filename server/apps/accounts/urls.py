from django.urls import path
from apps.accounts.views import (
    AccountUserRegistration,
    AccountUserLogin,
    AccountUserInfo,
    AccountUserLogout,
    AccountUserRefresh,
)

urlpatterns = [
    path('register/', AccountUserRegistration.as_view(), name='register'),
    path('login/', AccountUserLogin.as_view(), name='login'),
    path('logout/', AccountUserLogout.as_view(), name='logout'),
    path('info/', AccountUserInfo.as_view(), name='info'),
    path("refresh/", AccountUserRefresh.as_view(), name='refresh')
]