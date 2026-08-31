from django.urls import path

from .views import (
    BillingProducts,
    BillingSubscription,
    BillingSubscribe,
)


urlpatterns = [
    path('products/', BillingProducts.as_view(), name = 'billing_products'),
    path('business/<uuid:business_id>/', BillingSubscription.as_view(), name = 'billing_subscription'),
    path('business/<uuid:business_id>/subscribe/', BillingSubscribe.as_view(), name = 'billing_subscribe'),
]