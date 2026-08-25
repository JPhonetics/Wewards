from django.urls import path
from apps.businesses.views import (
    BusinessRegister,
)

urlpatterns = [
    path('register/', BusinessRegister.as_view(), name='register'),
]

