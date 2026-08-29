from rest_framework.response import Response
from rest_framework import status

from djstripe.models import (
    Customer,
    Price,
)


"""
## Called from BusinessRegister view
## When a new business is registered we need to make them 
## a billing customer and start their trial
"""

def create_billing_customer(business):
    
    # new business should not have a customer record
    # however, if they do this will cover it.
    customer, created = Customer.get_or_create(
        subscriber = business,
    )

    return customer


def create_trial_subscription(billing_customer):
    
    # docker compose exec backend python manage.py shell
    # without .first(), query returns a query set
    base_price = Price.objects.filter(
        product__name = "Wewards",
        metadata__nickname = "base_price",
    ).first()
    
    # We are setting base_price as the subscription price with a 30-day
    # for a trial. This allows us to not collect card information
    # during signup
    subscription = billing_customer.subscribe(
        price = base_price,
        trial_period_days = 30
    )
    
    return subscription