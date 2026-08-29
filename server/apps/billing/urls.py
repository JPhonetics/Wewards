from django.urls import path
from .views import BillingProducts


urlpatterns = [
    path('products/', BillingProducts.as_view(), name = 'billing_products'),
]