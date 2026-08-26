from django.urls import path
from apps.accounts.views import (
    AccountUserSignup,
    AccountUserLogin,
    AccountUserInfo,
    AccountUserRefresh,
    AccountUserPassword,
    AccountUserLogout,
)

urlpatterns = [
    path('signup/', AccountUserSignup.as_view(), name = 'account_signup'),
    path('login/', AccountUserLogin.as_view(), name = 'account_login'),
    path('user/', AccountUserInfo.as_view(), name = 'account_user'),
    path("refresh/", AccountUserRefresh.as_view(), name = 'account_refresh'),
    path("password/", AccountUserPassword.as_view(), name = "account_password"),
    path('logout/', AccountUserLogout.as_view(), name = 'account_logout'),
]