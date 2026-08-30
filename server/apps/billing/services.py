import stripe
from django.conf import settings
from django.core.exceptions import ValidationError
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


def get_billing_customer(business):
    
    try:
        customer = Customer.objects.get(
            subscriber = business,
        )
    
    except Customer.DoesNotExist:
        raise ValidationError(
            "Billing Customer does not exist."
        )
    
    return customer


def get_business_subscriptions_all(business):
    
    billing_customer = get_billing_customer(business)
    
    subscriptions = billing_customer.subscriptions.order_by(
        '-created'
    )
    
    return subscriptions


def get_business_subscription_latest(business):
    
    billing_customer = get_billing_customer(business)
    
    subscription = billing_customer.subscriptions.order_by(
        '-created'
    ).first()
    
    
    return subscription


def get_billing_price(
    price_id,
):
    
    try:
        price = Price.objects.get(
            id = price_id
        )
        
    except Price.DoesNotExist:
        raise ValidationError(
            "Billing Price does not exist."
        )
    
    return price


def get_subscription_item(
    subscription,
):
    
    # Get the first item (row) on the subscription
    # May have multiple items if addons were offered on top of base plan
    subscription_item = subscription.items.first()
    
    if not subscription_item:
        raise ValidationError(
            "Subscription Item does not exist."
        )
    
    return subscription_item


def get_subscription_price(
    subscription,
):
    
    subscription_item = get_subscription_item(subscription)

    # Get the Price attached to that subscription item
    price = subscription_item.price
    
    return price


def create_subscription_checkout(
    billing_customer,
    subscription,
    price,
    success_url,
    cancel_url,
):
    
    # Get the current item attached to this subscription
    subscription_item = get_subscription_item(subscription)
    
    # Update the existing trial subscription to use
    # the Price selected by the user
    stripe.Subscription.modify(
        subscription.id,
        items = [
            {
                'id': subscription_item.id,
                'price': price.id,
            }
        ],
        api_key = settings.STRIPE_TEST_SECRET_KEY,
    )
    
    # Create a Stripe-hosted Checkout page
    # setup mode collects payment information without charging yet
    checkout = stripe.checkout.Session.create(
        customer = billing_customer.id,
        mode = 'setup',
        success_url = success_url,
        cancel_url = cancel_url,
        setup_intent_data = {
            'metadata': {
                # Lets us know which subscription this setup belongs to
                'subscription_id': subscription.id,
            }
        },
        api_key = settings.STRIPE_TEST_SECRET_KEY,
    )
    
    return checkout